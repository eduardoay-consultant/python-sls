"""Boostrap the environment."""

from typing import Callable, Dict, Optional

from .env_file import load_env_file, load_from_remote
from .defaults import set_defaults


def bootstrap(
    env_file: Optional[str] = ".env",
    remote: Optional[Callable[..., Dict[str, str]]] = None,
    defaults: Optional[Dict[str, str]] = None,
) -> None:
    """Bootstrap the environment.

    Args:
        env_file (str, optional): The path to the environment file. Defaults to
            '.env'.
        remote (Callable[..., Dict[str, str]], optional): A callback function
            that returns a dictionary of environment variables. Defaults to
            None.
        defaults (Dict[str, str], optional): A dictionary of environment
            variables and default values. Defaults to None.
    """

    remote_vars = {}

    if remote is not None:
        remote_vars = remote()

    if env_file not in ["", None] and not remote_vars:
        load_env_file(env_file)
    else:
        load_from_remote(lambda: remote_vars)

    if defaults is not None:
        set_defaults(defaults)
