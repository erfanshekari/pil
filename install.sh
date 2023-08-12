#!/bin/bash

python3 -m venv env
env/bin/pip install -r requirements.txt
ln -s "$(pwd)/pil.py" /bin/pil
pil --help