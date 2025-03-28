#!/bin/ash

echo "Apply databse migrations"

python manage.py migrate

exec "$@"