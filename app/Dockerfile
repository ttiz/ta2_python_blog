FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /init/
COPY requirements.txt /init

WORKDIR /init/
RUN pip install -r requirements.txt