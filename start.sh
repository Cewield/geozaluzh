#!/bin/bash
echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating superuser..."
python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123456')
    print('Superuser created')
else:
    print('Superuser already exists')
"

echo "Starting Gunicorn..."
gunicorn geozaluz.wsgi --bind 0.0.0.0:$PORT