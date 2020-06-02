FROM        python:3.8-alpine

ADD         src /

RUN         apk update \
            && pip install --upgrade pip
RUN         apk add --no-cache --virtual .build-deps build-base mariadb-dev \
            && apk add --no-cache mariadb-connector-c-dev
RUN         pip install -r requirements.txt \
            && pip install gunicorn
RUN         apk del .build-deps

ENV         MODU_PRODUCTION = "True"

EXPOSE      8086

ENTRYPOINT  python manage.py makemigrations \
            && python manage.py migrate \
            && gunicorn --bind=0.0.0.0:8086 MODU.wsgi