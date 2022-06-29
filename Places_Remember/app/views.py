from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

from .models import Impression


def login(request):
    return render(request, 'login.html')


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def add_impression(request):
    pass

