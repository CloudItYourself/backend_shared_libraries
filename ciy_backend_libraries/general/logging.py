import logging
from typing import Final
from axiom_logger import AxiomHandler

from ciy_backend_libraries.environment.env_supplier import EnvironmentSupplier

LOGGING_FORMAT: Final[str] = "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"


def initialize_logger(logger_name: str):
    formatter = logging.Formatter(LOGGING_FORMAT)
    logger_details = EnvironmentSupplier().get_axiom_logger_details()
    axiom_handler = AxiomHandler(logger_details.dataset, logger_details.api_token)
    axiom_handler.setLevel(logging.INFO)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.addHandler(axiom_handler)
