web: gunicorn recruto.wsgi:application --log-file - --log-level debug  --forwarded-allow-ips="10.170.3.217,10.170.3.220"
python manage.py collectstatic --noinput
manage.py migrate