"""Defines signal-function for showing sub state column of units table.
"""
from ...constants import WIDGETS


def on_sub_state_toggled(widget, app_instance):
    """Signal-function for showing sub state column of units table.

    Parameters
    ----------
    widget: Gtk.Widget
        Widget of the checked checkbutton.
    app_instance: Application
        Instance of application whereby signal will be executed.
    """
    sub_state_column_widget = WIDGETS.get('sub_state_col')
    is_sub_state_visible = widget.get_active()

    app_instance.builder.get_object(sub_state_column_widget)\
                   .set_visible(is_sub_state_visible)
