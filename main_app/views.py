from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Finch, Toy
from .form import FeedingForm


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
    feeding_form = FeedingForm()
    toys_finch_doesnt_have = Toy.objects.exclude(id__in=finch.toys.all().values_list('id'))
    return render(request, 'finchs/detail.html', { 
        'finch': finch, 
        'feeding_form': feeding_form,
        'toys': toys_finch_doesnt_have
    })


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

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('finchs_detail', finch_id=finch_id)

class ToyList(ListView):
  model = Toy

class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'

class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys/'

def assoc_toy(request, finch_id, toy_id):
  finch = Finch.objects.get(id=finch_id)
  finch.toys.add(toy_id)
  return redirect('finchs_detail', finch_id=finch_id)

