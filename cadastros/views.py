from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Clientes

#Redirecionamento da página
from django.urls import reverse_lazy

class ClientesCad(CreateView):
    model = Clientes
    fields = ['nome','email','telefone']
    template_name = 'cadastros/index_cadastros.html'
    success_url = reverse_lazy('listagem')
    
class ClientesListagem(ListView):
    model = Clientes
    template_name = 'cadastros/listar_cadastro.html'
    
# Pagina editar
class ClientesUpdate(UpdateView):
    model = Clientes
    fields = "__all__"
    template_name = 'cadastros/index_cadastros.html'
    success_url = reverse_lazy('listagem')

#Pagina Deletar
class ClientesDelete(DeleteView):
    model = Clientes
    template_name = 'cadastros/excluir_cadastros.html'
    success_url = reverse_lazy('listagem')
    
def abertura_modelForm(request):
    return render(render, "index.html")