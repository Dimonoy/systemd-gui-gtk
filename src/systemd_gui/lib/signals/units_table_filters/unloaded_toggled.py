"""Defines signal-function for updating `units_filters` unloaded option.
"""
from ...constants import WIDGETS


def on_unloaded_toggled(widget, app_instance):
    """Signal-function for updating `units_filters` unloaded option.

    Parameters
    ----------
    widget: Gtk.Widget
        Widget of the checked checkbutton.
    app_instance: Application
        Instance of application whereby signal will be executed.
    """
    widget_state = widget.get_active()

    app_instance.units_filters.update({'unloaded': widget_state})
    masked_chk_widget = WIDGETS.get('units')\
                               .get('masked_chk')

    masked_chk = app_instance.builder.get_object(masked_chk_widget)
    masked_chk.set_sensitive(not widget_state)

    app_instance.update_units_store()
