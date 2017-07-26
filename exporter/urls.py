# exporter/urls.py
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.report, name='report'),
    url(r'^meta/', views.display_meta, name='display_meta')
]
