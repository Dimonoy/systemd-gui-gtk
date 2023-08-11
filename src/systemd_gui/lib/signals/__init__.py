"""Initializes signal-functions.
"""
from .systemd.apply_clicked import on_apply_clicked
from .systemd.reset_clicked import on_reset_clicked
from .systemd.alter_clicked import on_alter_clicked

from .units_table_filters.user_toggled import on_user_toggled
from .units_table_filters.inactive_toggled import on_inactive_toggled
from .units_table_filters.unloaded_toggled import on_unloaded_toggled
from .units_table_filters.masked_toggled import on_masked_toggled

from .view_options.toolbar_toggled import on_toolbar_toggled
from .view_options.load_state_toggled import on_load_state_toggled
from .view_options.active_state_toggled import on_active_state_toggled
from .view_options.sub_state_toggled import on_sub_state_toggled
from .view_options.description_toggled import on_description_toggled

from .combo_box_changed import on_combo_box_changed
from .search_changed import on_search_changed

from .about import on_about
from .quit import on_quit

__all__ = (
    on_apply_clicked,
    on_reset_clicked,
    on_alter_clicked,

    on_user_toggled,
    on_inactive_toggled,
    on_unloaded_toggled,
    on_masked_toggled,

    on_toolbar_toggled,
    on_load_state_toggled,
    on_active_state_toggled,
    on_sub_state_toggled,
    on_description_toggled,

    on_combo_box_changed,
    on_search_changed,

    on_about,
    on_quit,
)
