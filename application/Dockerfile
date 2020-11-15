FROM python:3.6-alpine

LABEL MAINTAINER="Zebra Zeal <bram@launchai.io>"

RUN echo "BUILDING BUILD:" $BUILD

RUN adduser -D zebrazeal
WORKDIR /home/zebrazeal

COPY requirements.txt requirements.txt
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install --upgrade pip
RUN python -m venv venv
RUN venv/bin/pip install --upgrade pip
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY run.py config.py boot.sh ./
RUN chmod +x boot.sh

RUN chown -R zebrazeal:zebrazeal ./
USER zebrazeal

EXPOSE 5000
ENTRYPOINT [ "./boot.sh" ]