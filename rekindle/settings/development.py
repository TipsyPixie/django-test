# noinspection ALL
from .default import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gVuRG403XdM0bWjpurEJVhuK29WIS4aoFdirUXm6NZC/SGHGcGEZH4t8XAvtU16dFlPoPhcYjGMWZj67L/rEteMYo2XxrKmN91xEMw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

CONN_MAX_AGE = 5

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rekindle_dev',
        'USER': 'developer',
        'PASSWORD': 'IAmThouThouArtI',
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'client_encoding': 'UTF8'
        },
    }
}

# Caches
# https://docs.djangoproject.com/en/2.1/ref/settings/#caches

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://localhost:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# Sessions
# https://docs.djangoproject.com/en/2.1/ref/settings/#sessions

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
