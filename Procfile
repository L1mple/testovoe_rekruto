web: gunicorn recruto.wsgi:application --log-file - --log-level debug  --host 0.0.0.0 --port $PORT
python manage.py collectstatic --noinput
manage.py migrate