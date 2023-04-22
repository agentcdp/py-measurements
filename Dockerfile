FROM python:3.8
ENV PYTHONUNBUFFERED 1

# App setup
ADD . /app
WORKDIR /app

# Requirements installation
RUN pip install -r requirements.txt
