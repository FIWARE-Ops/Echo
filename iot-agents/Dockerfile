FROM python:3.7.3-alpine3.9
LABEL maintainer="Dmitrii Demin <mail@demin.co>"

WORKDIR /opt/

COPY . /opt/

RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/bin/env", "python3", "-u", "/opt/run.py"]
