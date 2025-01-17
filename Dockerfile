# Docker image
FROM python:3.9.4

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/