release: python manage.py makemigrations --noinput && python manage.py migrate --noinput
web: gunicorn ocupy.wsgi --log-file -