"""Defines signal-function for setting `current_combo_box_selection` with the current combo box selection content.
"""


def on_combo_box_changed(widget, app_instance):
    """Signal-function for setting `current_combo_box_selection` with the current combo box selection content.

    Parameters
    ----------
    widget: Gtk.Widget
        Widget of a combo box.
    app_instance: Application
        Instance of application whereby signal will be executed.
    """
    app_instance.current_combo_box_selection = widget.get_child().get_text()

    app_instance.update_units_store()
