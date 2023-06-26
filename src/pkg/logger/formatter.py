"""Formatter interface."""

from typing import Dict, AnyStr, Any, Union


class Formatter:
    """Is a Logger Formatter implementation."""

    def format(
        self,
        logger_name: str,
        message: str,
        level: str,
        fields: Dict[AnyStr, Any],
        error: Union[Exception, None],
    ) -> str:
        """Format the message.

        :type logger_name: str
        :param logger_name: The name of the logger.

        :type message: str
        :param message: The message to format.

        :type fields: Dict[AnyStr, Any]
        :param fields: The log fields.

        :type level: str
        :param level: The log level.

        :type error: Union[Exception, None]
        :param error: possible error on the logs

        :return: The formatted message.
        """

        raise NotImplementedError
