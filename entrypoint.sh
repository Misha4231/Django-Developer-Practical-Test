#!/bin/sh

cd CVProject

echo "Running database migrations..."
poetry run python manage.py migrate --noinput

echo "Collecting static files..."
poetry run python manage.py collectstatic --noinput

echo "Starting Gunicorn..."
exec poetry run gunicorn CVProject.wsgi:application --bind 0.0.0.0:8000