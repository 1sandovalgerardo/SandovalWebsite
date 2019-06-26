from django.shortcuts import render
from django.views.generic import View
from django.views.generic import TemplateView

# Create your views here.

class SamplesView(TemplateView):
    template_name = 'samples.html'
