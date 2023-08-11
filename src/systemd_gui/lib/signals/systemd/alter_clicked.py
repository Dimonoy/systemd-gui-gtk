"""Defines signal-function for extending `actions_chain` with units state change commands.
"""
from ...constants import WIDGETS


def on_alter_clicked(widget, app_instance):
    """Signal-function for extending `actions_chain` with units state change commands.

    Parameters
    ----------
    widget: Gtk.Widget
        Widget of a clicked button.
    app_instance: Application
        Instance of application whereby signal will be executed.
    """
    command_type = widget.props.label.lower()
    units_store_widget = WIDGETS.get('store').get('units')
    units_selection_widget = WIDGETS.get('units').get('selection')

    store = app_instance.builder.get_object(units_store_widget)
    _, paths = app_instance.builder.get_object(units_selection_widget)\
                                   .get_selected_rows()

    for path in paths:
        iter_ = store.get_iter(path)
        unit_name = store.get_value(iter_, 0)
        app_instance.actions_chain.append((unit_name, command_type))
