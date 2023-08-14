"""Defines application class and application execution script.

Application class (aka. View Model, assembles project to application) comprises of:
    - UI (aka. View, GTK .glade files to define application components, styles, signal names and constant rules);
    - signals (aka. Commands, defines usable components behavior);
    - systemd proxy (aka. Proxy, controls limited systemd actions).
"""
import gi

try:
    gi.require_version('Gtk', '3.0')
    from gi.repository import Gtk, GLib, GObject
except ImportError:
    raise Exception('No Gtk 3.0, GLib or GObject in your system! Try to install...')

from .lib import SystemdProxy, UserSystemdProxy, Settings
from .lib.constants import APPLICATION_PATH, WIDGETS
from .lib.structures import PageType

from .lib.signals import on_apply_clicked, on_reset_clicked, on_alter_clicked
from .lib.signals import on_user_toggled, on_unloaded_toggled, on_inactive_toggled, on_masked_toggled
from .lib.signals import on_toolbar_toggled, on_load_state_toggled, on_active_state_toggled,\
                         on_sub_state_toggled, on_description_toggled
from .lib.signals import on_combo_box_changed, on_search_changed
from .lib.signals import on_about, on_quit


class Application(Gtk.Application):
    """Application class (aka. View Model)

    Attributes
    ----------
    settings: Settings
        Settings for application.
    builder: Gtk.Builder
        Root application builder to grasp UI components.
    systemd: SystemdProxy
        Systemd proxy class for systemd interactions.
    window: Gtk.ApplicationWindow
        Main window for the application to present to user.
    stack: Gtk.Stack
        Stack widget (component) for navigation monitoring.
    actions_chain: array_like
        Mutable list of `(unit_name, command_type)` entries for further systemd commands execution.
    units_filters: dict
        Filters for units table.
    current_search_entry: str
        Mutable string with search entry content.
    current_combo_box_selection: str
        Mutable string with combo box selection content.
    signals: dict
        Map of defined in UI (.glade files) signal names and `(signal_functions, application_instance)`.
    """

    def __init__(self):
        from gi.repository.GLib import set_application_name

        self.settings = Settings()
        settings = self.settings.get_settings()

        app_id, app_name = settings.get('app').get('id'), settings.get('app').get('name')

        super().__init__(application_id=app_id)
        set_application_name(app_name)

        stack_widget = WIDGETS.get('stack')

        self.builder = Gtk.Builder.new_from_file(str(APPLICATION_PATH))

        self.systemd = SystemdProxy()

        self.window = None
        self.stack = self.builder.get_object(stack_widget)

        self.actions_chain = []
        self.units_filters = {'user': False,
                              'unloaded': False,
                              'inactive': False,
                              'masked': False}

        self.current_search_entry = ''
        self.current_combo_box_selection = ''

        self.signals = {'onApplyButtonClicked': (on_apply_clicked, self),
                        'onResetButtonClicked': (on_reset_clicked, self),
                        'onStartButtonClicked': (on_alter_clicked, self),
                        'onStopButtonClicked': (on_alter_clicked, self),
                        'onReloadButtonClicked': (on_alter_clicked, self),
                        'onRestartButtonClicked': (on_alter_clicked, self),
                        'onEnableButtonClicked': (on_alter_clicked, self),
                        'onDisableButtonClicked': (on_alter_clicked, self),
                        'onMaskButtonClicked': (on_alter_clicked, self),
                        'onUnmaskButtonClicked': (on_alter_clicked, self),

                        'onApplyActivate': (on_apply_clicked, self),
                        'onResetActivate': (on_reset_clicked, self),
                        'onStartActivate': (on_alter_clicked, self),
                        'onStopActivate': (on_alter_clicked, self),
                        'onReloadActivate': (on_alter_clicked, self),
                        'onRestartActivate': (on_alter_clicked, self),
                        'onEnableActivate': (on_alter_clicked, self),
                        'onDisableActivate': (on_alter_clicked, self),
                        'onMaskActivate': (on_alter_clicked, self),
                        'onUnmaskActivate': (on_alter_clicked, self),
                        #'onManPageActivate': (, self),
                        'onQuitActivate': (on_quit, self),

                        'onRefreshActivate': self.update,
                        'onToolbarToggled': (on_toolbar_toggled, self),
                        'onLoadStateToggled': (on_load_state_toggled, self),
                        'onActiveStateToggled': (on_active_state_toggled, self),
                        'onSubStateToggled': (on_sub_state_toggled, self),
                        'onDescriptionToggled': (on_description_toggled, self),

                        'onAboutActivate': (on_about, self),

                        'onUnitsSearchChanged': (on_search_changed, self),
                        'onUnitsUserToggled': (on_user_toggled, self),
                        'onUnitsUnloadedToggled': (on_unloaded_toggled, self),
                        'onUnitsInactiveToggled': (on_inactive_toggled, self),
                        'onUnitsMaskedToggled': (on_masked_toggled, self),
                        'onUnitsComboBoxChanged': (on_combo_box_changed, self),

                        'onConfigsSearchChanged': (on_search_changed, self),

                        'onPageChange': self.update}

    def update_systemd_proxy(self):
        """Switches systemd proxy type.
        """
        is_user = self.units_filters.get('user')

        self.systemd = SystemdProxy() if not is_user else UserSystemdProxy()

    def update_total(self, obj, total):
        """Updates total widget (component) content.

        Parameters
        ----------
        obj: Gtk.Label
            Total label widget (component).
        total: int
            Current total amount of records in a table.
        """
        total_obj = self.builder.get_object(obj)
        label = f'Total: {total}'
        total_obj.set_label(label)

    def update_status(self, obj, status):
        """Updates status widget (component) content.

        Parameters
        ----------
        obj: Gtk.Label
            Status label widget (component).
        status: str
            Status text.
        """
        status_obj = self.builder.get_object(obj)
        status_obj.set_label(status.capitalize())

    def update_configs_store(self):
        """Updates configs list store widget (component).
        """
        configs_store_widget = WIDGETS.get('store').get('configs')
        configs_total_widget = WIDGETS.get('configs').get('total')

        configs_store = self.builder.get_object(configs_store_widget)
        configs_store.clear()

        for row in self.systemd.get_configs():
            configs_store.append(row)

        self.update_total(configs_total_widget, len(configs_store))

    def update_units_store(self):
        """Updates units list store widget (component).
        """
        names, states = [], (self.units_filters.get('unloaded') * 'not-found',
                             self.units_filters.get('inactive') * 'inactive',
                             self.units_filters.get('masked') * 'masked')
        units_store_widget = WIDGETS.get('store').get('units')
        units_total_widget = WIDGETS.get('units').get('total')

        units_store = self.builder.get_object(units_store_widget)
        units_store.clear()

        names = names if self.current_search_entry == '' else [f'*{self.current_search_entry}*']
        names = names if self.current_combo_box_selection in ('', 'all') \
            else names + [f'*.{self.current_combo_box_selection}']

        states = filter(lambda state: state != '', states)
        states = list(states)

        for row in self.systemd.get_units(states=states, names=names):
            units_store.append(row)

        self.update_total(units_total_widget, len(units_store))

    def update(self, *_):
        """Updates current page's list store.
        """
        page_name = self.stack.get_visible_child_name()

        if page_name is None:
            return

        current_page = PageType.to_proto(page_name)

        if current_page == PageType.UNITS:
            self.update_units_store()
        elif current_page == PageType.CONFIGS:
            self.update_configs_store()
        elif current_page == PageType.TIMERS:
            # store = self.builder.get_object(WIDGETS.get('store').get('timers'))
            pass
        elif current_page is None:
            pass

        GObject.timeout_add(30000, self.update)

    def _init_window(self):
        """Initializes and present window.
        """
        if not self.window:
            self.window = self.builder.get_object(WIDGETS.get('app_win'))
            self.window.set_application(self)

        self.window.present()

    def _init_view_options(self):
        """Initializes view options' toggles.
        """
        settings = self.settings.get_settings()
        menu_view = WIDGETS.get('menu').get('view')
        units_table = settings.get('units_table')

        self.builder.get_object(menu_view.get('toolbar_chk'))\
                    .set_active(settings.get('toolbar').get('show'))

        self.builder.get_object(menu_view.get('load_state_chk'))\
                    .set_active(units_table.get('load_state_column').get('show'))

        self.builder.get_object(menu_view.get('active_state_chk'))\
                    .set_active(units_table.get('active_state_column').get('show'))

        self.builder.get_object(menu_view.get('sub_state_chk'))\
                    .set_active(units_table.get('sub_state_column').get('show'))

        self.builder.get_object(menu_view.get('desc_chk'))\
                    .set_active(units_table.get('description_column').get('show'))

    def _init_units_filters(self):
        """Initializes `units_filters`.
        """
        settings = self.settings.get_settings()
        units_filters = settings.get('units_filters')

        self.units_filters.update({'user': units_filters.get('user').get('checked'),
                                   'unloaded': units_filters.get('unloaded').get('checked'),
                                   'inactive': units_filters.get('inactive').get('checked'),
                                   'masked': units_filters.get('masked').get('checked')})

    def do_startup(self):
        """On application start connects signals.
        """
        Gtk.Application.do_startup(self)
        self.builder.connect_signals(self.signals)

    def do_activate(self):
        """On application activation (after startup) runs initializations.

        Initializes:
            - window;
            - view options;
            - units filters.
        """
        self._init_window()
        self._init_view_options()
        self._init_units_filters()


def main():
    """Executes application.
    """
    import sys

    app = Application()
    sys.exit(app.run(sys.argv))
