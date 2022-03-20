from dataclasses import field
from urllib import request
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DeleteView, View
from .forms import *
#from .models import ProjetosModel

#Redirecionamento da página
from django.urls import reverse_lazy

class CriarProjeto(CreateView):
  template_name="index.html"
  model = ProjetosModel
  fields = '__all__'
  
def create(request):
  form = ProjetosForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('index.html')
