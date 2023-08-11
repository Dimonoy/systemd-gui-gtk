"""Defines logger abstract.
"""
from abc import ABC, abstractmethod
from .singleton import SingletonMeta


class LoggerBase(ABC, metaclass=SingletonMeta):
    @staticmethod
    @abstractmethod
    def from_logger(*args, **kwargs): pass

    @staticmethod
    @abstractmethod
    def from_params(*args, **kwargs): pass

    @abstractmethod
    def info(self, *args, **kwargs): pass

    @abstractmethod
    def debug(self, *args, **kwargs): pass

    @abstractmethod
    def warn(self, *args, **kwargs): pass

    @abstractmethod
    def close(self): pass
