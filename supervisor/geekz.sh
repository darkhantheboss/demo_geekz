#!/bin/bash

cd /srv/projects/geekz
exec /srv/envs/geekz/bin/gunicorn geekz.wsgi -b 127.0.0.1:8034  --timeout=120 -w 1