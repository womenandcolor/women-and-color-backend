FROM python:3-slim
MAINTAINER Mark Gituma <mark.gituma@gmail.com>

ENV PROJECT_ROOT /app
WORKDIR $PROJECT_ROOT

RUN apt-get update -y \
    && apt-get install -y libjpeg62 libjpeg62-turbo-dev zlib1g-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py runserver 0.0.0.0:8000

