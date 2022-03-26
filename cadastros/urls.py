from pipes import Template
from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', CriarProjeto.as_view(), name='cadastro-de-projetos' ),
    path('listagem/', ProjetosListagem.as_view(), name='listagem-de-projetos' ),
    path('update/<int:pk>', EditarProjeto.as_view() , name='editar-projeto'),
    path('deletar/<int:pk>', DeletarProjeto.as_view() , name='deletar-projeto'),
]