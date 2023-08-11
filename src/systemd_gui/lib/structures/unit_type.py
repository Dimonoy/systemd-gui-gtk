"""Defines unit type structure.
"""
from enum import IntEnum
from ..errors import NoProtoAssigned


class UnitType(IntEnum):
    """Unit type enumerate.

    Attributes
    ----------
    ALL: int
    SERVICE: int
    SOCKET: int
    TIMER: int
    PATH: int
    TARGET: int
    SCOPE: int
    SLICE: int
    AUTOMOUNT: int
    MOUNT: int
    DEVICE: int
    SWAP: int
    """
    ALL = 0
    SERVICE = 1
    SOCKET = 2
    TIMER = 3
    PATH = 4
    TARGET = 5
    SCOPE = 6
    SLICE = 7
    AUTOMOUNT = 8
    MOUNT = 9
    DEVICE = 10
    SWAP = 11

    @classmethod
    def from_proto(cls, proto):
        """Converts prototype to string prototype.

        Parameters
        ----------
        proto: UnitType
            UnitType prototype.

        Returns
        -------
        str
            String version of prototype.

        Raises
        ------
        NoProtoAssigned
            If a given prototype if not defined.
        """
        if proto == cls.ALL:
            return 'all'
        if proto == cls.SERVICE:
            return 'service'
        if proto == cls.SOCKET:
            return 'socket'
        if proto == cls.TIMER:
            return 'timer'
        if proto == cls.PATH:
            return 'path'
        if proto == cls.TARGET:
            return 'target'
        if proto == cls.SCOPE:
            return 'scope'
        if proto == cls.SLICE:
            return 'slice'
        if proto == cls.AUTOMOUNT:
            return 'automount'
        if proto == cls.MOUNT:
            return 'mount'
        if proto == cls.DEVICE:
            return 'device'
        if proto == cls.SWAP:
            return 'swap'
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
        UnitType
            UnitType prototype.

        Raises
        ------
        NoProtoAssigned
            If a given prototype if not defined.
        """
        if name == 'all':
            return cls.ALL
        if name == 'service':
            return cls.SERVICE
        if name == 'socket':
            return cls.SOCKET
        if name == 'timer':
            return cls.TIMER
        if name == 'path':
            return cls.PATH
        if name == 'target':
            return cls.TARGET
        if name == 'scope':
            return cls.SCOPE
        if name == 'slice':
            return cls.SLICE
        if name == 'automount':
            return cls.AUTOMOUNT
        if name == 'mount':
            return cls.MOUNT
        if name == 'device':
            return cls.DEVICE
        if name == 'swap':
            return cls.SWAP
        raise NoProtoAssigned(f'No `{name}` assigned to the `{cls.__name__}` enumerate.')
