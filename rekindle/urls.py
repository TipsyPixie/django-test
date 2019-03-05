"""rekindle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

Note:
    This app uses flask-style URL pattern
    https://github.com/afg984/django-fsu
"""

from django.contrib import admin
from django.urls import include
from django_fsu import url
from rest_framework.schemas import get_schema_view

import lightstage

urlpatterns = [
    url(path='admin/', view=admin.site.urls),
    url(path='schema/', view=get_schema_view(title='Rekindle API', description='Temporary API')),
    url(path='', view=include(lightstage.urls)),
]
