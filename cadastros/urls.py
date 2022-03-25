from pipes import Template
from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    # path('', TemplateView.as_view(template_name='index.html'), name='index' ),
    path('', CriarProjeto.as_view(), name='cadastro-de-projetos' ),
    path('listagem/', ProjetosListagem.as_view(), name='listagem-de-projetos' ),
]