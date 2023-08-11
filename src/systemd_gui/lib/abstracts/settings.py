"""Defines settings abstract.
"""
from abc import ABC, abstractmethod
from .singleton import SingletonMeta


class SettingsBase(ABC, metaclass=SingletonMeta):
    @abstractmethod
    def get_settings(self, *args, **kwargs): pass

    @abstractmethod
    def set_settings(self, *args, **kwargs): pass

    @abstractmethod
    def reset_settings(self, *args, **kwargs): pass
