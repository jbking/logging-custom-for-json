import logging
from logging.config import fileConfig
from pythonjsonlogger import jsonlogger


class CJsonFormatter(jsonlogger.JsonFormatter):
    pass


old_factory = logging.getLogRecordFactory()


def record_factory(*args, **kwargs):
    # print("args", args)
    # print("kwargs", kwargs)
    record = old_factory(*args, **kwargs)
    return record


def setup_logging(conf_path):
    fileConfig(conf_path)
    logging.setLogRecordFactory(record_factory)
