FROM python:3.8.12-slim-buster
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir /expenzo-be
WORKDIR /expenzo-be
COPY requirements.txt .
RUN apt-get update && apt-get --fix-missing install -y \
    #Required to install mysqlclient
    default-libmysqlclient-dev \
    #Required to build wheels for mysqlclient and uwsgi
    gcc
RUN pip3 install -r requirements.txt
COPY . .

