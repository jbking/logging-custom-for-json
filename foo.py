from uuid import uuid4
import logging
from logging_exam.logging import setup_logging


setup_logging("log.conf")
logger = logging.getLogger("custom")
logger.info("hello", extra={"context_id": str(uuid4())})
logger.info("foo")
