"""Is a Logger Formatter"""
from datetime import datetime
from typing import Dict, AnyStr, Any, Union

from colored import Fore, Style

from src.pkg.logger.formatter import Formatter
from src.pkg.logger.utils import get_stack_trace


class ColoredFormatter(Formatter):
    """Formatter that outputs a colored string."""

    def format(
        self,
        logger_name: str,
        message: str,
        level: str,
        fields: Dict[AnyStr, Any],
        error: Union[Exception, None],
    ) -> str:
        """Format the fields into a colored string.

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

        new_fields = {}

        trace = None

        if error is not None:
            new_fields["error"] = str(error)
            trace = get_stack_trace(error)

        merged_fields = {**new_fields, **fields}

        if trace is not None:
            merged_fields["stack"] = trace

        name_format = _format_field("service", logger_name)
        timestamp_format = _format_field("timestamp", datetime.utcnow().isoformat())
        msg_format = _format_field("message", message)
        level_format = _format_field("level", level)

        fields_format = " ".join(
            [_format_field(key, value) for key, value in merged_fields.items()]
        )

        return f"{timestamp_format} {level_format} {name_format} {msg_format} {fields_format}"


def _format_field(key: AnyStr, value: Any) -> str:
    """Format a field.

    :type key: AnyStr
    :param key: The field key.

    :type value: Any
    :param value: The field value.

    :rtype: str
    :return: The formatted field.
    """

    if key in ["error", "stack"]:
        return f"{Fore.red}{key}{Style.reset}{Fore.grey_70}={Style.reset}{Fore.grey_93}{value}{Style.reset}"

    return f"{Fore.cyan}{key}{Style.reset}{Fore.grey_70}={Style.reset}{Fore.grey_93}{value}{Style.reset}"
