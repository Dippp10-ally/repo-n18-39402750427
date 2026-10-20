"""Small logging helpers."""

import logging


def get_logger(name="app"):
    """Return a configured logger with a console handler."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
