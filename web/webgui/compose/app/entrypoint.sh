#!/bin/bash

set -e

echo "${0}: running migrations."
python manage.py migrate --noinput

echo "${0}: collecting statics."

python manage.py runserver 0.0.0.0:9081