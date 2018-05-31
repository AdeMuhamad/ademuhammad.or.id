FROM python:3

RUN mkdir /usr/app
WORKDIR /usr/app
ADD . /usr/app

RUN pip install -r requirements.txt