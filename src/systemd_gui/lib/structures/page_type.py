"""Defines page type structure.
"""
from enum import IntEnum
from ..errors import NoProtoAssigned


class PageType(IntEnum):
    """Page type enumerate.

    Attributes
    ----------
    UNITS: int
    CONFIGS: int
    TIMERS: int
    """
    UNITS = 0
    CONFIGS = 1
    TIMERS = 2

    @classmethod
    def from_proto(cls, proto):
        """Converts prototype to string prototype.

        Parameters
        ----------
        proto: PageType
            PageType prototype.

        Returns
        -------
        str
            String version of prototype.

        Raises
        ------
        NoProtoAssigned
            If a given prototype if not defined.
        """
        if proto == cls.UNITS:
            return 'UnitsPage'
        if proto == cls.CONFIGS:
            return 'ConfigsPage'
        if proto == cls.TIMERS:
            return 'TimersPage'
        raise NoProtoAssigned(f'No `{proto}` assigned to the `{cls.__name__}` enumerate.')

    @classmethod
    def to_proto(cls, name):
        """Converts string prototype to prototype.

        Parameters
        ----------
        name: str
            String version of prototype.

        Returns
        -------
        PageType
            PageType prototype.

        Raises
        ------
        NoProtoAssigned
            If a given prototype if not defined.
        """
        if name == 'UnitsPage':
            return cls.UNITS
        if name == 'ConfigsPage':
            return cls.CONFIGS
        if name == 'TimersPage':
            return cls.TIMERS
        raise NoProtoAssigned(f'No `{name}` assigned to the `{cls.__name__}` enumerate.')
