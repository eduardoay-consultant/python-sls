"""main logger instance"""
from typing import Union

from .logger import Logger
from .formatter import Formatter
from .json_formatter import JsonFormatter
from .colored_formatter import ColoredFormatter
from .bootstrap import get, bootstrap
