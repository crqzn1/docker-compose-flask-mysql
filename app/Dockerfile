# FROM python:3.6
# FROM python:3.7-alpine3.13
# FROM python:3.7
FROM python:3.7-slim

EXPOSE 9000

COPY .  /app
WORKDIR /app

# COPY requirements.txt /app
# COPY static/favicon.ico /app/static
RUN pip install -r requirements.txt

COPY app.py /app
CMD python app.py
