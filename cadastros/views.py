from dataclasses import field
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import *
#from .models import ProjetosModel



#Redirecionamento da página
from django.urls import reverse_lazy

def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = ProjetosForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
    return render(request, "index.html", context)