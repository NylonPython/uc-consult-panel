from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^login/', views.login_view, name='login_view'),
    url(r'^login/go', views.login, name='login'),
]
