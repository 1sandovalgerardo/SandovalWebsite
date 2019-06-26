# -*- coding: utf-8 -*-

from django.conf.urls import url
from AppAboutMe import views

app_name = 'aboutme'

urlpatterns = [url(r'^$', views.AboutMeView.as_view(), name='aboutme')]