# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY car_rest_api .