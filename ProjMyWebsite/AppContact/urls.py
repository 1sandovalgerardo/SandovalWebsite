# -*- coding: utf-8 -*-

from django.conf.urls import url
from AppContact import views

app_name = 'contact'

urlpatterns = [url(r'^$', views.ContactMeView.as_view(), name='contactme')]
