"""
WSGI config for rekindle project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

env = os.environ.setdefault('REKINDLE_ENV', 'development')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'rekindle.settings.{env}')

application = get_wsgi_application()
