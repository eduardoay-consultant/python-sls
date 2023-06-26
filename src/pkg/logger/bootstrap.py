"""Bootstrap the logger package."""
from typing import AnyStr

from .formatter import Formatter

from .logger import Logger

log = Logger(name="service")


def get() -> Logger:
    """Get the logger instance.

    :rtype: Logger
    :return: The logger instance.
    """

    global log
    return log


def bootstrap(name: AnyStr, level: int, formatter: Formatter) -> None:
    """Bootstrap the logger package.

    :type name: AnyStr
    :param name: The name of the logger.

    :type level: int
    :param level: The logging level.

    :type formatter: Formatter
    :param formatter: The formatter to use.
    """

    global log

    log = Logger(name=name, level=level)
    log.set_formatter(formatter)
