#!/usr/bin/env bash
pip3 install pytest
pip3 install coverage

python3 project/app/main.py
coverage run -m pytest project/