"""Utility functions for the logger package."""
import traceback


def get_stack_trace(error: Exception) -> list[str]:
    """Get the stack trace from the error.

    :type error: Exception
    :param error: The error.

    :rtype: str
    :return: The stack trace.
    """

    return traceback.format_tb(error.__traceback__)
