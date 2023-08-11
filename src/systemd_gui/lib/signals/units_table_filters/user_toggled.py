"""Defines signal-function for updating `units_filters` user option.
"""


def on_user_toggled(widget, app_instance):
    """Signal-function for updating `units_filters` user option.

    Parameters
    ----------
    widget: Gtk.Widget
        Widget of the checked checkbutton.
    app_instance: Application
        Instance of application whereby signal will be executed.
    """
    app_instance.units_filters.update({'user': widget.get_active()})

    app_instance.update_systemd_proxy()
    app_instance.update_units_store()
