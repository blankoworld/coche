#!/usr/bin/env bash
virtualenv --no-site-packages --distribute venv && source venv/bin/activate && pip install -r requirements.txt
