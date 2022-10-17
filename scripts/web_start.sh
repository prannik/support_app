#!/bin/sh

set -o errexit
set -o nounset

#./manage.py flush --noinput
#echo "Db cleared"

./manage.py migrate --noinput
echo "Models migrated"

./manage.py loaddata fixtures/*.json
echo "Loaded fixtures"

./manage.py collectstatic --noinput
echo "Static collected"

gunicorn -w 3 -b :8000 config.wsgi:application

./ manage.py runserver 0.0.0.0:8000