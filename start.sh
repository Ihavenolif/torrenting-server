#!/bin/bash

apt update
apt upgrade -y
apt install python3 python3-pip rtorrent
pip3 install flask
python3 app.py