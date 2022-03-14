from dataclasses import field
from django.shortcuts import render
from django.views.generic import CreateView
from .forms import *
#from .models import ProjetosModel

#Redirecionamento da página
from django.urls import reverse_lazy

class create_view(CreateView):
  template_name="index.html"
  model = ProjetosModel
  fields = [
            'title',
            'description',
        ]