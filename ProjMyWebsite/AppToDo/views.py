from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic import TemplateView

# Create your views here.


class ToDoList(TemplateView):
    template_name = 'todolist.html'

