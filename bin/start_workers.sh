#!/usr/bin/env bash

celery --version 2>&1 >> /dev/null || (echo 'celery not found. did you forget to activate venv?'; exit 1;)

celery multi start 2 -c 2 -A rekindle
celery beat -A rekindle --detach -f beat.log --pidfile beat.pid

