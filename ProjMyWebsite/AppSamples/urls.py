# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from AppSamples import views

app_name = 'samples'

urlpatterns = [url(r'^$', views.SamplesView.as_view(), name='samples'),
               url(r'^todolist/', include('AppToDo.urls')),
               ]