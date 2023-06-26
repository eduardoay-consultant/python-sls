"""Functions to load environment variables from a file."""
import os
from typing import Callable, Dict

from dotenv import load_dotenv


def load_env_file(path: str) -> None:
    """Load environment variables from a file.

    Args:
        path (str): The path to the environment file.

    Raises:
        FileNotFoundError: If the environment file is not found.
    """

    if not os.path.isfile(path):
        raise FileNotFoundError(f"Environment file not found: {path}")

    load_dotenv(path)


def load_from_remote(callback: Callable[..., Dict[str, str]]) -> None:
    """Load environment variables from a remote source.

    Args:
        callback (Callable[..., Dict[str, str]]): A callback function that
            returns a dictionary of environment variables.
    """

    env = callback()

    for name, value in env.items():
        if name not in os.environ:
            os.environ[name] = value
