#!/usr/bin/env bash

pip install -r requirements.txt

cd Backend

python manage.py collectstatic --noinput

python manage.py migrate