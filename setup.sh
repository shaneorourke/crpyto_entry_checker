#!bin/bash

python3 -m venv crypto &&
source crypto/bin/activate &&
pip install -r requirements.txt &&
python setup.py &&
deactivate