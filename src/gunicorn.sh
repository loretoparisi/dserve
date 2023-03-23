#!/bin/sh
gunicorn --chdir /app api:app -w 4 -k uvicorn.workers.UvicornWorker -c gunicorn_conf.py