FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir /expenzo-be
WORKDIR /expenzo-be
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

