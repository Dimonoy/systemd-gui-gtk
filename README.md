# Systemd GUI Gtk

[![Python Version](https://img.shields.io/badge/python-=>3.8-brightgreen)](https://python.org/)
[![Conventional Commits](https://img.shields.io/badge/conventional_commits-1.0.0-yellow)](https://python.org/)

Software for managing systemd through user interface. The application is built upon PyGObject (Gtk 3.0).

> [__INFO__] Currently supports only python package, rpm build is planned.

---

## Preparation
1) Clone the repository and change directory to the downloaded project.

2) Prepare python virtual environment:
```bash
$ python -m venv <virtual-environment-name>
```

3) Install requirements:
```bash
$ pip install -r requirements.txt
```

4) Run build:
```bash
$ python -m build
```

## Installation
Install project from the built distribution tar gzip:
```bash
$ pip install dist/<file-name>.tar.gz
```
> [__WARNING__] Make sure to exit from the virtual environment for package to be installed in the global site-packages.

## Usage
To run CLI version of the application:
```bash
$ systemd-cli
```

To run GUI version of the application (you can create desktop file refering to this command as the execution command):
```bash
$ systemd-gui
```

## License
[Apache License 2.0](LICENSE).
