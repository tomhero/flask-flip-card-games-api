FROM python:3.7.6-alpine

# Label for this image
LABEL maintainer="Chayut Ruksomya <chayut.191@gmail.com>"

# set work directory
WORKDIR /usr/src/app

# set environment variables
# PYTHONDONTWRITEBYTECODE: Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED: Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
# because of connection for mongo altas
RUN pip install pymongo[srv]

# copy project
COPY . /usr/src/app/