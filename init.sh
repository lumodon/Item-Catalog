#!/bin/sh
sudo -H pip install virtualenv
virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
python ./database/lotsofitems.py
