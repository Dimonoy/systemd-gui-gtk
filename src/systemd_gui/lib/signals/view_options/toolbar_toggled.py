"""Defines signal-function for showing toolbar on units page.
"""
from ...constants import WIDGETS


def on_toolbar_toggled(widget, app_instance):
    """Signal-function for showing toolbar on units page.

    Parameters
    ----------
    widget: Gtk.Widget
        Widget of the checked checkbutton.
    app_instance: Application
        Instance of application whereby signal will be executed.
    """
    toolbar_widget = WIDGETS.get('toolbar')
    is_toolbar_visible = widget.get_active()

    app_instance.builder.get_object(toolbar_widget)\
                   .set_visible(is_toolbar_visible)
