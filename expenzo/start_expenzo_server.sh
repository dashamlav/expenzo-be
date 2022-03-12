#!/bin/bash

export PROJECT_PATH=`pwd`

echo "Making migrations..."
python manage.py migrate --no-input

echo "Starting expenzo django server..."
uwsgi --static-map /static=$PROJECT_PATH/static --ini $PROJECT_PATH/uwsgi.ini
