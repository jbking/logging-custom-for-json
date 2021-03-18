import logging
import sys
from uuid import uuid4

from loguru import logger

from logging_exam.bar_logging import log_out


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


def main():
    logging.basicConfig(handlers=[InterceptHandler()], level=0)
    # logging.basicConfig(level=0)

    logger.remove()
    logger.add(sys.stderr, serialize=True)

    logger.info("main")

    log_out("1")
    log_out("2")
    log_out("3", additional_context={"context": "dummy"})

    with logger.contextualize(context=str(uuid4())):
        log_out("4")
        log_out("5", additional_context={"context": "dummy2"})
        log_out("6", additional_context={"another_context": "dummy_another"})
        log_out("7")

    log_out("8")


if __name__ == '__main__':
    main()
