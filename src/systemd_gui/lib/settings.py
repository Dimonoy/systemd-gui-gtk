"""Defines settings for the application.
"""
import yaml

from json import dumps

from .abstracts import SettingsBase
from .constants import SETTINGS_PATH, DEFAULT_SETTINGS_PATH


class Settings(SettingsBase):
    """Settings for the application.

    This class reads settings from the .yaml file in the local etc directory. If no settings file found in the
    local etc directory, it reads default settings file in the local etc directory.

    Attributes
    ----------
    _settings: dict
        Map of settings read from a .yaml file.
    settings_path: pathlib.Path
        Path to the settings .yaml file.
    """
    def __init__(self):
        self._settings = None
        self.settings_path = None

        if not SETTINGS_PATH.exists():
            from shutil import copyfile

            copyfile(str(DEFAULT_SETTINGS_PATH), str(SETTINGS_PATH))

        self.settings_path = SETTINGS_PATH

        with open(str(self.settings_path), 'r') as f:
            self._settings = yaml.safe_load(f)

    def __str__(self):
        return dumps(self._settings, indent=2)

    def get_settings(self):
        """Returns settings.

        Returns
        -------
        dict
            Settings.
        """
        return self._settings

    def set_settings(self, new_settings, permanently=False):
        """Set new defined by user settings.

        Parameters
        ----------
        new_settings: dict
            New defined settings by user.
        permanently: bool, optional
            Whether to save settings to the settings .yaml file.
        """
        self._settings.update(new_settings)

        if permanently:
            with open(str(SETTINGS_PATH), 'w') as f:
                yaml.dump(self._settings, f)

    def reset_settings(self, permanently=False):
        """Resets settings to the default.

        Parameters
        ----------
        permanently: bool, optional
            Whether to reset settings in the settings .yaml file.
        """
        with open(str(DEFAULT_SETTINGS_PATH), 'r') as f:
            default_settings = yaml.safe_load(f)

        self._settings = default_settings

        if permanently:
            with open(str(SETTINGS_PATH), 'w') as f:
                yaml.dump(default_settings, f)
