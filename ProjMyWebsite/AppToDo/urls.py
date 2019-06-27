# -*- coding: utf-8 -*-
from django.conf.urls import url
from AppToDo import views

app_name = 'todolist'

urlpatterns = [url(r'^$', views.ToDoListView, name='todolist'),
               url(r'^delete/(?P<pk>\d+)', views.Delete, name='delete'),
               ]
