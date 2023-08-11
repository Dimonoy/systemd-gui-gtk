"""Defines signal-function for setting `current_search_entry` with the current search entry's content.
"""


def on_search_changed(widget, app_instance):
    """Signal-function for setting `current_search_entry` with the current search entry's content.

    Parameters
    ----------
    widget: Gtk.Widget
        Widget of a search entry.
    app_instance: Application
        Instance of application whereby signal will be executed.
    """
    app_instance.current_search_entry = widget.props.text

    app_instance.update()
