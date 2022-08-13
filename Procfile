web: gunicorn recruto.wsgi:application --log-file - --log-level debug  --bind=127.0.0.1
python manage.py collectstatic --noinput
manage.py migrate