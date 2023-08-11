#!/bin/bash

source ./venv/bin/activate

# Not working well, do not install python package
python setup.py bdist_rpm --no-autoreq