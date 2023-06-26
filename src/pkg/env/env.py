"""Environment variables manager that follows the 12-factor app guidelines.
"""
import os
from typing import Union

from .defaults import defaults


def get(name: str) -> Union[str, None]:
    """Get the value of an environment variable.

    Args:
        name (str): The name of the environment variable.

    Returns:
        str: The value of the environment variable or the default value.
    """

    val = os.environ.get(name, None)

    if val is None:
        val = defaults.get(name, None)

    return val


def get_str(name: str) -> str:
    """Get the value of an environment variable as a string.

    Args:
        name (str): The name of the environment variable.

    Returns:
        str: The value of the environment variable or the default value.
    """

    return get(name)


def get_int(name: str) -> int:
    """Get the value of an environment variable as an integer.

    Args:
        name (str): The name of the environment variable.

    Returns:
        int: The value of the environment variable or the default value.
    """

    return int(get(name))


def get_float(name: str) -> float:
    """Get the value of an environment variable as a float.

    Args:
        name (str): The name of the environment variable.

    Returns:
        float: The value of the environment variable or the default value.
    """

    return float(get(name))


def get_bool(name: str) -> bool:
    """Get the value of an environment variable as a boolean.

    Args:
        name (str): The name of the environment variable.

    Returns:
        bool: The value of the environment variable or the default value.
    """

    return get(name).lower() in ["true", "1", "yes"]


def get_list(name: str) -> list:
    """Get the value of an environment variable as a list.

    Args:
        name (str): The name of the environment variable.

    Returns:
        list: The value of the environment variable or the default value.
    """

    return get(name).split(",")


def get_dict(name: str) -> dict:
    """Get the value of an environment variable as a dictionary.

    Args:
        name (str): The name of the environment variable.

    Returns:
        dict: The value of the environment variable or the default value.
    """

    return dict(item.split(":") for item in get_list(name))
