# -*- coding: utf-8 -*-

from django.conf.urls import url
from AppBlog import views

app_name = 'blog'

urlpatterns = [url(r'^$', views.BlogView.as_view(), name='blog')]
