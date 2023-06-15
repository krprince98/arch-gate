# syntax=docker/dockerfile:1
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y python3 python3-pip

RUN mkdir /arch-gate
WORKDIR /arch-gate

COPY requirements.txt .
RUN mkdir src
COPY src src
RUN pip install -r requirements.txt

ENV FLASK_APP=src/archg
RUN flask create-db
CMD flask run --host 0.0.0.0
