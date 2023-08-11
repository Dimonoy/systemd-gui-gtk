"""Defines systemd proxies.
"""
from gi.repository import Gio
from gi.repository.GLib import Variant

from .structures import UnitCommandType
from .abstracts import SystemdProxyBase

from pathlib import Path
from re import match


class SystemdProxy(SystemdProxyBase):
    """Systemd proxy by system dbus.

    Attributes
    ----------
    _iface: Gio.DBusProxy
        Proxy object for systemd commands interactions through dbus.
    """
    def __init__(self):
        self._iface = None
        self._set_dbus(Gio.BusType.SYSTEM)

    def __str__(self):
        return self._iface

    def _set_dbus(self, bus_type_object):
        """Initializes `_iface` proxy.

        Parameters
        ----------
        bus_type_object: Gio.BusType
            DBus type.
        """
        bus = Gio.bus_get_sync(bus_type=bus_type_object,
                               cancellable=None)

        self._iface = Gio.DBusProxy.new_sync(connection=bus,
                                             flags=Gio.DBusProxyFlags.NONE,
                                             info=None,
                                             name='org.freedesktop.systemd1',
                                             object_path='/org/freedesktop/systemd1',
                                             interface_name='org.freedesktop.systemd1.Manager',
                                             cancellable=None)

    @staticmethod
    def _build_get_units_condition(states, names):
        """Creates string condition for filtering units output.

        Parameters
        ----------
        states: array_like
            List of states.
        names: array_like
            List of unit names.

        Returns
        -------
        str
            String condition for filtering units output.
        """
        condition = ''

        if len(states) > 1:
            load_state = 'not-found' if 'not-found' in states else 'masked'
            condition = f'unit[2] == \'{load_state}\' and unit[3] == \'inactive\''

        if len(names) > 1:
            unit_name, unit_type = f'.{names[0][:-1]}.*', f'.{names[1]}'
            match_ = f'match(\'{unit_name}\', unit[0]) is not None and match(\'{unit_type}\', unit[0]) is not None'
            condition = match_ if condition == '' else f'{condition} and {match_}'

        return condition

    def get_units(self, states, names):
        """Requests units records.

        Parameters
        ----------
        states: array_like
            List of states.
        names: array_like
            List of unit names.

        Yields
        ------
        array_like
            Tuple of unit's record.
        """
        # [NOTE] Stopped and disabled units are not shown following from the current script. In systemctl, there is
        # an option --all, that allows to show all the units regardless the state it in.
        # [TODO:FIX] make command to list all units (including stopped & disabled)
        condition = self._build_get_units_condition(states=states,
                                                    names=names)

        if condition != '':
            for unit in self._iface.ListUnitsByPatterns('(asas)', states, names):
                if eval(condition):
                    yield unit[0], unit[2], unit[3], unit[4], unit[1]
        else:
            for unit in self._iface.ListUnitsByPatterns('(asas)', states, names):
                yield unit[0], unit[2], unit[3], unit[4], unit[1]

    @staticmethod
    def get_configs():
        """Requests units configs files.

        Yields
        ------
        array_like
            Tuple of unit's config path and unit's dependant.
        """
        for entry in Path('/etc/systemd/system').glob('*/*'):
            wanted_by = entry.parent.name

            if wanted_by.endswith(('wants', 'requires')):
                yield entry.name, '.'.join(wanted_by.split('.')[:-1])
            else:
                yield entry.name, None

        for entry in Path('/etc/systemd/system').glob('*'):
            if entry.is_file():
                yield entry.name, None

    def get_timers(self):
        """Requests timers.

        [NOTE] There is no such a command to receive all timers in systemd dbus api. The only way is to request
        each timer unit individual (check https://www.freedesktop.org/wiki/Software/systemd/dbus#timerunitobjects)
        [TODO] Request and yield timers.
        """
        pass

    @staticmethod
    def get_systemd_dbus_method_parameters(unit_name, command_type):
        """Selects systemd command and systemd command parameters.

        Parameters
        ----------
        unit_name: str
            Unit name.
        command_type: str, UnitCommandType
            Command type.

        Returns
        -------
        array_like
            Tuple of systemd command and systemd command parameters.
        """
        if type(command_type) is str:
            command_type = UnitCommandType.to_proto(command_type)

        if command_type == UnitCommandType.START:
            return 'StartUnit', Variant('(ss)', (unit_name, 'replace'))
        if command_type == UnitCommandType.STOP:
            return 'StopUnit', Variant('(ss)', (unit_name, 'replace'))
        if command_type == UnitCommandType.RELOAD:
            return 'ReloadUnit', Variant('(ss)', (unit_name, 'replace'))
        if command_type == UnitCommandType.RESTART:
            return 'RestartUnit', Variant('(ss)', (unit_name, 'replace'))
        if command_type == UnitCommandType.ENABLE:
            return 'EnableUnitFiles', Variant('(asbb)', ([unit_name], False, True))
        if command_type == UnitCommandType.DISABLE:
            return 'DisableUnitFiles', Variant('(asb)', ([unit_name], False))
        if command_type == UnitCommandType.MASK:
            return 'MaskUnitFiles', Variant('(asbb)', ([unit_name], False, True))
        if command_type == UnitCommandType.UNMASK:
            return 'UnmaskUnitFiles', Variant('(asb)', ([unit_name], False))

    def alter_unit(self, unit_name, command_type):
        """Runs systemd command.

        Parameters
        ----------
        unit_name: str
            Unit name.
        command_type: str, UnitCommandType
            Command type.

        Returns
        -------
        int
            Systemd return signal.
        """
        method_name, parameters = self.get_systemd_dbus_method_parameters(unit_name=unit_name,
                                                                          command_type=command_type)

        return self._iface.call_sync(method_name=method_name,
                                     parameters=parameters,
                                     flags=Gio.DBusCallFlags.ALLOW_INTERACTIVE_AUTHORIZATION,
                                     timeout_msec=-1,
                                     cancellable=None)


class UserSystemdProxy(SystemdProxy):
    """Systemd proxy by user dbus.
    """
    def __init__(self):
        super().__init__()
        self._set_dbus(Gio.BusType.SESSION)
