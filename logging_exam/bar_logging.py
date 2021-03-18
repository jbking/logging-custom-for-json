import logging

from loguru import logger


_logger = logging.getLogger(__name__)


def log_out(msg, additional_context=None):
    if additional_context is None:
        logger.info("logging out")
        _logger.info("logging.logger out")
    else:
        with logger.contextualize(**additional_context):
            logger.info("logging out with-in context")
            _logger.info("logging.logger out with-in context")

