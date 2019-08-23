#!/usr/bin/env sh

if [[ -n "$1" ]]; then workers=$2; else workers=4; fi

echo "Starting with ${workers} workers"

for i in $(seq 1 ${workers}); do
    su -s /bin/sh - nginx -c "/usr/bin/env python3 -u /opt/run.py --path /tmp/echo${i}.sock &"
    echo "server unix:/tmp/echo${i}.sock fail_timeout=2;" >> /tmp/upstream.conf
done

nginx -g "daemon off;"
