#!/bin/sh
gunicorn --chdir /app dserve.api:app -w 4 --preload -k uvicorn.workers.UvicornWorker -c gunicorn_conf.py