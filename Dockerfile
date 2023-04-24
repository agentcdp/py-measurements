FROM python:3.8
ENV PYTHONUNBUFFERED 1

# App setup
ADD . /app
WORKDIR /app

# Requirements installation
RUN pip install -r requirements.txt

# Running the app
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
