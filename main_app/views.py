from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Finch


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finchs_index(request):
    finchs = Finch.objects.all()
    return render(request, 'finchs/index.html', { 'finchs': finchs })

def finchs_detail(request, finch_id):
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finchs/detail.html', { 'finch': finch })

class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'
    success_url = '/finchs/'

class FinchUpdate(UpdateView):
    model = Finch 
    fields = ['size', 'description', 'age']

class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finchs/'


