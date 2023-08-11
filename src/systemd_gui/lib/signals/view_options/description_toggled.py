"""Defines signal-function for showing description column of units table.
"""
from ...constants import WIDGETS


def on_description_toggled(widget, app_instance):
    """Signal-function for showing description column of units table.

    Parameters
    ----------
    widget: Gtk.Widget
        Widget of the checked checkbutton.
    app_instance: Application
        Instance of application whereby signal will be executed.
    """
    description_column_widget = WIDGETS.get('desc_col')
    is_description_visible = widget.get_active()

    app_instance.builder.get_object(description_column_widget)\
                   .set_visible(is_description_visible)
