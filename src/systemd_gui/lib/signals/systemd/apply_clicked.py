"""Defines signal-function for execution of `actions_chain` systemd commands.
"""


def on_apply_clicked(widget, app_instance):
    """Signal-function for execution of `actions_chain` systemd commands.

    Parameters
    ----------
    widget: Gtk.Widget
        Widget of the clicked apply button.
    app_instance: Application
        Instance of application whereby signal will be executed.
    """
    for action in app_instance.actions_chain:
        unit_name, command_type = action

        if command_type is not None:
            app_instance.systemd.alter_unit(unit_name=unit_name,
                                       command_type=command_type)

    app_instance.actions_chain.clear()
    app_instance.update_units_store()
