# -*- coding: utf-8 -*-

from django.conf.urls import url
from AppIndex import views

app_name = 'index'

urlpatterns = [url(r'^$', views.IndexView.as_view(), name='index')]