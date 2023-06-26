"""JSON formatter for the logger."""

import json
from typing import AnyStr, Any, Dict, Union
from datetime import datetime

from .formatter import Formatter
from .utils import get_stack_trace


class JsonFormatter(Formatter):
    """Formatter that outputs a JSON string."""

    def format(
        self,
        logger_name: str,
        message: str,
        level: str,
        fields: Dict[AnyStr, Any],
        error: Union[Exception, None],
    ) -> str:
        """Format the fields into a JSON string.

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

        timestamp = datetime.utcnow().isoformat()

        new_fields = {
            "timestamp": timestamp,
            "level": level,
            "service": logger_name,
            "message": message,
        }

        trace = None

        if error is not None:
            new_fields["error"] = str(error)
            trace = get_stack_trace(error)

        merged_fields = {**new_fields, **fields}

        if trace is not None:
            merged_fields["stack"] = trace

        return json.dumps(merged_fields)
