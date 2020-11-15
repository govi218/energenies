#!/bin/sh
source venv/bin/activate
exec gunicorn -w 4 --bind 0.0.0.0:5000 run
