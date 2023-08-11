"""Defines signal-function for resetting (clearing) `actions_chain`.
"""


def on_reset_clicked(widget, app_instance):
    """Signal-function for resetting (clearing) `actions_chain`.

    Parameters
    ----------
    widget: Gtk.Widget
        Widget of the clicked apply button.
    app_instance: Application
        Instance of application whereby signal will be executed.
    """
    app_instance.actions_chain.clear()

    app_instance.update_units_store()
