"""LaundryBear URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from rest_framework.authtoken import views as rest_views
from api.views import ObtainAuthToken#obtain_auth_token, ObtainAuthToken

import api
import client
import management

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^management/', include('management.urls', namespace='management')),
    url(r'^', include('client.urls', namespace='client')),
    url(r'^api/', include('api.urls')),
    url(r'^api/auth/', include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api-token-auth/', rest_views.obtain_auth_token),
    url(r'^api/token-auth$', api.views.GetAuthToken.as_view())#api.views.obtain_auth_token),
]