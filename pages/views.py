from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
     return render(request, 'pages/index.html')

def about(request):
     return render(request, 'pages/about.html')

def index(request):
     return render(request, 'pages/index.html')

def bootstrap(request):
     return render(request, 'pages/bootstrap.html')

