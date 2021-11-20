from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

class HomeTemplateView(TemplateView):
    template_name = 'index.html'
