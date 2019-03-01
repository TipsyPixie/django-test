# noinspection ALL
from .default import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gVuRG403XdM0bWjpurEJVhuK29WIS4aoFdirUXm6NZC/SGHGcGEZH4t8XAvtU16dFlPoPhcYjGMWZj67L/rEteMYo2XxrKmN91xEMw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Application definition

INSTALLED_APPS.insert(0, 'debug_toolbar')

MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')

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

# Debug toolbar
# https://django-debug-toolbar.readthedocs.io/en/latest/

INTERNAL_IPS = ['127.0.0.1', 'localhost']

# Prevent re-loader process from sharing the same log file
# https://stackoverflow.com/questions/26682413/django-rotating-file-handler-stuck-when-file-is-equal-to-maxbytes

if DEBUG and os.environ.get('RUN_MAIN', 'false') != 'true':
    LOGGING = {}
