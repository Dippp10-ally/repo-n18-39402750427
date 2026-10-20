import logging

from src.logging_utils import get_logger


def test_get_logger_returns_logger():
    logger = get_logger("example")
    assert isinstance(logger, logging.Logger)
