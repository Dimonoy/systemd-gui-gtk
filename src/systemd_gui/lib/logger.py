"""Defines logger.
"""
from .abstracts import LoggerBase


class Logger(LoggerBase):
    """Logger.
    """
    @staticmethod
    def from_logger(*args, **kwargs):
        pass

    @staticmethod
    def from_params(*args, **kwargs):
        pass

    def info(self, *args, **kwargs):
        pass

    def debug(self, *args, **kwargs):
        pass

    def warn(self, *args, **kwargs):
        pass

    def close(self):
        pass
