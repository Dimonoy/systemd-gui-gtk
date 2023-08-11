"""Defines signal-function for opening about window.
"""
import gi

try:
    gi.require_version('Gtk', '3.0')
    from gi.repository.Gtk import Builder
except ImportError:
    raise Exception('No Gtk 3.0, GLib or GObject in your system! Try to install...')

from ..constants import ABOUT_PATH, WIDGETS


def on_about(*_):
    """Signal-function for opening about window.
    """
    about_widget = WIDGETS.get('about')
    about_path = str(ABOUT_PATH)

    about_dialog = Builder.new_from_file(about_path)\
                          .get_object(about_widget)

    about_dialog.run()
    about_dialog.destroy()
