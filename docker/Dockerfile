FROM python:alpine
MAINTAINER nkoshell <nikita.koshelev@gmail.com>

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add postgresql-dev

RUN pip install --no-cache-dir tle_storage_service && apk del build-deps

EXPOSE 80
