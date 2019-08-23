FROM nginx:1.17.0-alpine
LABEL maintainer="Dmitrii Demin <mail@demin.co>"

WORKDIR /opt/

COPY . /opt/

RUN apk update && \
    apk add --no-cache python3-dev git build-base && \
    pip3 install -r requirements.txt && \
    apk del build-base git && \
    cp /opt/nginx.conf /etc/nginx/nginx.conf && \
    rm -Rf /var/cache/apk/*

ENTRYPOINT ["/opt/entrypoint.sh"]
