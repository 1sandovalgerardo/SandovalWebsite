# -*- coding: utf-8 -*-
from django.conf.urls import url
from AppToDo import views

app_name = 'todolist'

urlpatterns = [url(r'^$', views.ToDoListView, name='todolist'),
               url(r'^delete/(?P<pk>\d+)', views.Delete, name='delete'),
               url(r'^cross_off/(?P<pk>\d+)', views.cross_off, name='cross_off'),
               url(r'^uncross/(?P<pk>\d+)', views.uncross, name='uncross'),
               url(r'^edit/(?P<pk>\d+)', views.Edit, name='edit'),
               ]
