"""Logging levels."""

import logging
from enum import Enum


class Level(Enum):
    """Enum for logging levels."""

    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    FATAL = "fatal"


def level_name(level: int) -> str:
    """Get the name of the logging level.

    :type level: int
    :param level: The logging level.

    :rtype: str
    :return: The name of the logging level.
    """

    levels = {
        logging.DEBUG: Level.DEBUG.value,
        logging.INFO: Level.INFO.value,
        logging.WARNING: Level.WARNING.value,
        logging.ERROR: Level.ERROR.value,
        logging.FATAL: Level.FATAL.value,
    }

    return levels.get(level, Level.INFO.value)
