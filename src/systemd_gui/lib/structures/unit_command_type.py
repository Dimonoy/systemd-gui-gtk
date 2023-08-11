"""Defines unit command type structure.
"""
from enum import IntEnum
from ..errors import NoProtoAssigned


class UnitCommandType(IntEnum):
    """Unit command type enumerate.

    Attributes
    ----------
    START: int
    STOP: int
    RELOAD: int
    RESTART: int
    ENABLE: int
    DISABLE: int
    MASK: int
    UNMASK: int
    """
    START = 0
    STOP = 1
    RELOAD = 2
    RESTART = 3
    ENABLE = 4
    DISABLE = 5
    MASK = 6
    UNMASK = 7

    @classmethod
    def from_proto(cls, proto):
        """Converts prototype to string prototype.

        Parameters
        ----------
        proto: UnitCommandType
            UnitCommandType prototype.

        Returns
        -------
        str
            String version of prototype.

        Raises
        ------
        NoProtoAssigned
            If a given prototype if not defined.
        """
        if proto == cls.START:
            return 'start'
        if proto == cls.STOP:
            return 'stop'
        if proto == cls.RELOAD:
            return 'reload'
        if proto == cls.RESTART:
            return 'restart'
        if proto == cls.ENABLE:
            return 'enable'
        if proto == cls.DISABLE:
            return 'disable'
        if proto == cls.MASK:
            return 'mask'
        if proto == cls.UNMASK:
            return 'unmask'
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
        UnitCommandType
            UnitCommandType prototype.

        Raises
        ------
        NoProtoAssigned
            If a given prototype if not defined.
        """
        if name == 'start':
            return cls.START
        if name == 'stop':
            return cls.STOP
        if name == 'reload':
            return cls.RELOAD
        if name == 'restart':
            return cls.RESTART
        if name == 'enable':
            return cls.ENABLE
        if name == 'disable':
            return cls.DISABLE
        if name == 'mask':
            return cls.MASK
        if name == 'unmask':
            return cls.UNMASK
        raise NoProtoAssigned(f'No `{name}` assigned to the `{cls.__name__}` enumerate.')
