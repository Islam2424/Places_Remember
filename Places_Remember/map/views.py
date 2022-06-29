import django.views.generic
from django.shortcuts import render
from django.views.generic.base import TemplateView


class MapViews(TemplateView):
    '''Map View'''
    template_name = 'map.html'
