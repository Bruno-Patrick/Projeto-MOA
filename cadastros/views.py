from dataclasses import field
from urllib import request
from django.shortcuts import redirect
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from .forms import *
from django.urls import reverse_lazy

class CriarProjeto(CreateView):
  model = ProjetosModel
  fields = '__all__'
  template_name="index.html"
  sucess_url = reverse_lazy('listagem-de-projetos')

class ProjetosListagem(ListView):
  model = ProjetosModel
  template_name = 'app/listar_cadastros.html'

class EditarProjeto(UpdateView):
  model = ProjetosModel
  fields = "__all__" 
  template_name = 'app/index_cadastros.html'
  success_url = reverse_lazy('listagem-de-projetos')

class DeletarProjeto(DeleteView):
    model = ProjetosModel
    template_name = 'app/excluir_cadastros.html'
    success_url = reverse_lazy('listagem-de-projetos')