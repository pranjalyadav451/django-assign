#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python manage.py collectstatic --no-input
# python manage.py reset_db --noinput

python manage.py makemigrations

# to solve the 'auth group not found error on render.com'
python manage.py migrate auth
python manage.py migrate --run-syncdb

# to see the migrations in render.com console
# python manage.py showmigrations

# to solve the pkg_resources not found error
pip install --upgrade pip
pip install --force-reinstall -U setuptools