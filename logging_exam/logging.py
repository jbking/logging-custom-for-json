from logging.config import fileConfig


def setup_logging(conf_path):
    fileConfig(conf_path)
