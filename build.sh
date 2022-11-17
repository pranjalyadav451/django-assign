#!/usr/bin/env bash
# exit on error
set -o errexit

poetry install

python manage.py collectstatic --no-input
python manage.py makemigrations
python manage.py migrate auth
python manage.py migrate --run-syncdb
pip install --upgrade pip
python manage.py showmigrations
pip install --force-reinstall -U setuptools