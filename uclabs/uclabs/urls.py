"""uclabs URL Configuration

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
from django.conf.urls import include, url
from .admin import custom_admin
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls import patterns, include, url


urlpatterns = [
    url(r'^', include('blog.urls', namespace="blog")),
    url(r'^locations/', include('blog.locations-urls', namespace="locations")),
    url(r'^resources/', include('blog.resources-urls', namespace="resources")),
    url(r'^schedule/', include('schedule.urls')),
    url(r'^consult/', include(custom_admin.urls)),
]
