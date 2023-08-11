"""Defines signal-function for quiting the application.
"""


def on_quit(widget, app_instance):
    """Signal-function for quiting the application.

    Parameters
    ----------
    widget: Gtk.Widget
        Widget of the clicked button.
    app_instance: Application
        Instance of application whereby signal will be executed.
    """
    app_instance.quit()
