"""Defines signal-function for updating `units_filters` masked option.
"""
from ...constants import WIDGETS


def on_masked_toggled(widget, app_instance):
    """Signal-function for updating `units_filters` masked option.

    Parameters
    ----------
    widget: Gtk.Widget
        Widget of the clicked apply button.
    app_instance: Application
        Instance of application whereby signal will be executed.
    """
    widget_state = widget.get_active()

    app_instance.units_filters.update({'masked': widget_state})
    unloaded_chk_widget = WIDGETS.get('units')\
                                 .get('unloaded_chk')

    unloaded_chk = app_instance.builder.get_object(unloaded_chk_widget)
    unloaded_chk.set_sensitive(not widget_state)

    app_instance.update_units_store()
