"""Defines systemd proxy abstract.
"""
from abc import ABC, abstractmethod
from .singleton import SingletonMeta


class SystemdProxyBase(ABC, metaclass=SingletonMeta):
    @abstractmethod
    def get_units(self, *args, **kwargs): pass

    @staticmethod
    @abstractmethod
    def get_configs(*args, **kwargs): pass

    @abstractmethod
    def alter_unit(self, *args, **kwargs): pass
