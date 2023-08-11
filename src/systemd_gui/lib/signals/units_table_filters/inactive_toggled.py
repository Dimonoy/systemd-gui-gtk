"""Defines signal-function for updating `units_filters` inactive option.
"""


def on_inactive_toggled(widget, app_instance):
    """Signal-function for updating `units_filters` inactive option.

    Parameters
    ----------
    widget: Gtk.Widget
        Widget of the checked checkbutton.
    app_instance: Application
        Instance of application whereby signal will be executed.
    """
    app_instance.units_filters.update({'inactive': widget.get_active()})

    app_instance.update_units_store()
