#!/usr/bin/env bash

celery --version 2>&1 >> /dev/null || (echo 'celery not found. did you forget to activate venv?'; exit 1;)

sensible-browser 'http://localhost:5678' &
celery flower -A rekindle --port=5678 --broker_api=http://developer:IAmThouThouArtI@localhost:15672/api/
