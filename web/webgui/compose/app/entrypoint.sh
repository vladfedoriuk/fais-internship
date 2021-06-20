#!/bin/bash

set -e

find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

echo "${0}: running migrations."
python manage.py migrate --noinput

python manage.py initadmin

python manage.py createtokens

python manage.py test

python manage.py runserver 0.0.0.0:9081