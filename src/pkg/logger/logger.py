"""Package that holds structured logging functionality."""
import logging
from typing import Dict, AnyStr, Any, Union

from .formatter import Formatter
from .json_formatter import JsonFormatter
from .levels import level_name


class Logger:
    """Main class for structured logging."""

    _name: AnyStr
    _fields: Dict[AnyStr, Any]
    _context_fields: Dict[AnyStr, Any]
    _level: int
    _formatter: Formatter
    _error: Union[Exception, None]

    _logger: logging.Logger

    def __init__(self, name: AnyStr, level: int = logging.INFO) -> None:
        """Initialize the logger.

        :type name: AnyStr
        :param name: The name of the logger.

        :type level: int
        :param level: The logging level.
        """

        self._name = name
        self._level = level
        self._formatter = JsonFormatter()

        self.reset()

        self._init_logger()

    def set_formatter(self, formatter: Formatter) -> None:
        """Set the formatter.

        :type formatter: Formatter
        :param formatter: The formatter to set.

        :rtype: Logger
        :return: The logger.
        """

        self._formatter = formatter

    def fields(self, **kwargs) -> "Logger":
        """Set the log fields.

        :param kwargs: The fields to set.

        :rtype: Logger
        :return: The logger.
        """

        self._fields = {**self._fields, **kwargs}

        return self

    def context_fields(self, **kwargs) -> "Logger":
        """Set the context log fields.

        :param kwargs: The fields to set.

        :rtype: Logger
        :return: The logger.
        """

        self._context_fields = {**self._context_fields, **kwargs}

        return self

    def exception(self, error: Exception) -> "Logger":
        """Set the exception.

        :type error: Exception
        :param error: The exception to set.

        :rtype: Logger
        :return: The logger.
        """

        self._error = error

        return self

    def reset(self) -> None:
        """Reset the logger."""

        self._context_fields = {}
        self._reset()

    def debug(self, message: AnyStr) -> None:
        """Log a debug message.

        :type message: AnyStr
        :param message: The message to log.
        """

        self._log(logging.DEBUG, message)

    def info(self, message: AnyStr) -> None:
        """Log an info message.

        :type message: AnyStr
        :param message: The message to log.
        """

        self._log(logging.INFO, message)

    def warning(self, message: AnyStr) -> None:
        """Log a warning message.

        :type message: AnyStr
        :param message: The message to log.
        """

        self._log(logging.WARNING, message)

    def error(self, message: AnyStr) -> None:
        """Log an error message.

        :type message: AnyStr
        :param message: The message to log.
        """

        self._log(logging.ERROR, message)

    def fatal(self, message: AnyStr) -> None:
        """Log a fatal message.

        :type message: AnyStr
        :param message: The message to log.
        """

        self._log(logging.FATAL, message)

    def _log(self, level: int, message: AnyStr) -> None:
        """Log the message.

        :type level: AnyStr
        :param level: The log level.

        :type message: AnyStr
        :param message: The message to log.
        """

        fields = {**self._fields, **self._context_fields}

        formatted_log = self._formatter.format(
            logger_name=self._name,
            message=message,
            level=level_name(level),
            fields=fields,
            error=self._error,
        )

        self._logger.log(level, formatted_log)

        self._reset()

    def _reset(self) -> None:
        """Reset the logger."""

        self._fields = {}
        self._level = self._level
        self._error = None

    def _init_logger(self) -> None:
        """Initialize the logger."""

        log_format = logging.Formatter("%(message)s")

        logger = logging.getLogger(self._name)
        logger.setLevel(self._level)

        handler = logging.StreamHandler()
        handler.setFormatter(log_format)

        logger.addHandler(handler)

        self._logger = logger
