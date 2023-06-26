"""FastAPI app for AWS Lambda."""
import logging

from fastapi import FastAPI
from mangum import Mangum

from config import get_remote
from src.pkg import env
from src.pkg import logger


def get_formatter() -> logger.Formatter:
    """Get the log formatter.

    :rtype: logger.Formatter
    :return: The log formatter.
    """

    if env.get_str("STAGE") in ["dev", "prod"]:
        return logger.JsonFormatter()

    return logger.ColoredFormatter()


def get_log_level() -> int:
    """Get the log level.

    :rtype: int
    :return: The log level.
    """

    if env.get_bool("DEBUG"):
        return logging.DEBUG

    return logging.INFO


env.bootstrap(
    env_file=".env",
    remote=get_remote,
    defaults={
        "BASE_PATH": "",
    },
)

logger.bootstrap(
    name=env.get_str("APP_NAME"),
    level=get_log_level(),
    formatter=get_formatter(),
)

logger.get().info("Booting up...")

root_path = f"/{env.get_str('BASE_PATH')}"
api = FastAPI(title="FastAPI x AWS Lambda", root_path=root_path)


# ---------------------------------------------------------------------
# Routes


@api.get("/.health")
async def root():
    """Health check endpoint."""
    return {"message": "ok"}


handler = Mangum(api)
