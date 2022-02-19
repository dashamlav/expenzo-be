#!/bin/bash

export PROJECT_PATH=`pwd`
uwsgi --static-map /static=$PROJECT_PATH/static --ini $PROJECT_PATH/uwsgi.ini
