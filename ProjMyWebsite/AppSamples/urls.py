# -*- coding: utf-8 -*-

from django.conf.urls import url
from AppSamples import views

app_name = 'samples'

urlpatterns = [url(r'^$', views.SamplesView.as_view(), name='samples')]