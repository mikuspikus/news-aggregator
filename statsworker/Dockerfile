# pull official base image
FROM python:3.6.9-alpine

# set work directory
WORKDIR /usr/src/statsworker

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt /usr/src/statsworker/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/statsworker/
