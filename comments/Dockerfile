# pull official base image
FROM python:3.6.9-alpine

# set work directory
WORKDIR /usr/src/comments

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add --no-cache --virtual .build-deps python3-dev gcc build-base
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/comments/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/comments/entrypoint.sh

# copy project
COPY . /usr/src/comments/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/comments/entrypoint.sh"]
