from django.shortcuts import render
from django.http import HttpResponse
from .models import Finch


# Create your views here.

def home(request):
    return HttpResponse('<h1> Welcome to Finch Collector.</h1>')

def about(request):
    return render(request, 'about.html')

def finchs_index(request):
    finchs = Finch.objects.all()
    return render(request, 'finchs/index.html', { 'finchs': finchs })