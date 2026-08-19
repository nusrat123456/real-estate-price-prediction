#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

cd Backend
python manage.py collectstatic --noinput