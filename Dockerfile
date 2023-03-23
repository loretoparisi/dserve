#
# dserve
# @author Loreto Parisi (loretoparisi at gmail dot com)
# Copyright (c) 2023 Loreto Parisi (loretoparisi at gmail dot com)
#

FROM python:3.7.4-slim-buster

LABEL maintainer Loreto Parisi loretoparisi@gmail.com

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    curl

COPY src/requirements.txt /
RUN pip3 install -r requirements.txt

COPY ./src /app
WORKDIR /app

CMD ["./gunicorn.sh"]