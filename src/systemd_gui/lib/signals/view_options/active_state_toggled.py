"""Defines signal-function for showing active state column of units table.
"""
from ...constants import WIDGETS


def on_active_state_toggled(widget, app_instance):
    """Signal-function for showing active state column of units table.

    Parameters
    ----------
    widget: Gtk.Widget
        Widget of the checked checkbutton.
    app_instance: Application
        Instance of application whereby signal will be executed.
    """
    active_state_column_widget = WIDGETS.get('active_state_col')
    is_active_state_visible = widget.get_active()

    app_instance.builder.get_object(active_state_column_widget)\
                   .set_visible(is_active_state_visible)
