"""lightstage URL Configuration

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

from django_fsu import url

from lightstage import views

urlpatterns = [
    url(path='', view=views.index),
    url(path='sign_in/', view=views.auth.sign_in),
    url(path='sign_out/', view=views.auth.sign_out),
]
