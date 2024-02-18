import logging
from typing import Final
from axiom_logger import AxiomHandler


LOGGING_FORMAT: Final[str] = "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"


def initialize_logger(logger_name: str):
    formatter = logging.Formatter(LOGGING_FORMAT)
    axiom_handler = AxiomHandler('backend-logs', 'xaat-3ec687a1-e15c-488a-acba-4780b9f8ca62')
    axiom_handler.setLevel(logging.INFO)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.addHandler(axiom_handler)
