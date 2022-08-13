web: gunicorn recruto.wsgi:application --log-file - --log-level debug  --syslog_addr 0.0.0.0
python manage.py collectstatic --noinput
manage.py migrate