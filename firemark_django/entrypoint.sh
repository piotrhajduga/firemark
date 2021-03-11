#!/usr/bin/env sh
python manage.py migrate
exec "$@"