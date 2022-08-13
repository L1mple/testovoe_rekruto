web: gunicorn recruto.wsgi:application --log-file - --log-level debug  -b 0.0.0.0:8080
python manage.py collectstatic --noinput
manage.py migrate