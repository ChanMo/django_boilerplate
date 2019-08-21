FROM python:3

RUN apt-get update && apt-get install -y gettext

RUN mkdir /var/log/web
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --trusted-host mirrors.aliyun.com --index-url http://mirrors.aliyun.com/pypi/simple/ -r requirements.txt
