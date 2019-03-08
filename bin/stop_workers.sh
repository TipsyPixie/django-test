#!/usr/bin/env bash

celery --version 2>&1 >> /dev/null || (echo 'celery not found. did you forget to activate venv?'; exit 1;)

if [[ -f ./beat.pid ]]; then
    pkill --pidfile ./beat.pid
    rm ./beat.pid
fi
celery multi stop 2 --pidfile=celery%n.pid
