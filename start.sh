#!/bin/bash
echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Creating superuser if not exists..."
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123456')
    print("Superuser 'admin' created with password 'admin123456'")
else:
    print("Superuser already exists")
EOF

echo "Starting Gunicorn..."
gunicorn geozaluz.wsgi --bind 0.0.0.0:$PORT