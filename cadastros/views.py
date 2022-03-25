from dataclasses import field
from urllib import request
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DeleteView, ListView
from .forms import *
#from .models import ProjetosModel

#Redirecionamento da página
from django.urls import reverse_lazy

class CriarProjeto(CreateView):
  model = ProjetosModel
  fields = '__all__'
  template_name="index.html"
  sucess_url = reverse_lazy('index.html')

class ProjetosListagem(ListView):
  model = ProjetosModel
  template_name = 'app/listar_cadastros.html'