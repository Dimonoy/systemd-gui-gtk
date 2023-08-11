"""Defines paths within the project.
"""
from pathlib import Path


PROJECT_ROOT_PATH = Path(__file__).absolute().parent.parent.parent

CONFIGS_PATH = PROJECT_ROOT_PATH / 'etc'

APPLICATION_PATH = PROJECT_ROOT_PATH / 'ui' / 'application.glade'
ABOUT_PATH = PROJECT_ROOT_PATH / 'ui' / 'about.glade'

DEFAULT_SETTINGS_PATH = CONFIGS_PATH / 'default_settings.yaml'
SETTINGS_PATH = CONFIGS_PATH / 'settings.yaml'
