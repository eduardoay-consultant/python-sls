"""Default env configurations."""

defaults = {}


def set_default(name: str, value: str) -> None:
    """Set a default value for an environment variable.

    Args:
        name (str): The name of the environment variable.
        value (str): The default value of the environment variable.
    """

    defaults[name] = value


def set_defaults(defs: dict) -> None:
    """Set default values for environment variables.

    Args:
        defs (dict): A dictionary of environment variable names and default
            values.
    """

    for name, value in defs.items():
        set_default(name, value)
