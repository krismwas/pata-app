# pull official base image
FROM python:3.7.8-alpine3.12
#FROM python:3.5-alpine3.11
MAINTAINER cashmere ventures

WORKDIR /usr/pata-img/
# set environment variables
ENV PYTHONUNBUFFERED 1
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

#install dependecies
RUN pip install --upgrade pip

COPY ./requirement.txt .

RUN apk add --update --no-cache postgresql-client jpeg-dev python3-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r requirement.txt
RUN apk del .tmp-build-deps

# copy entrypoint.sh
COPY ./entrypoint.sh .

COPY ./src .

RUN mkdir -p /vol/web/mediafiles
RUN mkdir -p /vol/web/staticfiles

RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web

# run entrypoint.sh
ENTRYPOINT ["/usr/pata-img/entrypoint.sh"]

USER user