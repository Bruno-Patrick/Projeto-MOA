from pipes import Template
from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', CriarProjeto.as_view(), name='cadastro-de-projetos' ),
    path('', ProjetosListagem.as_view(), name='listagem' ),
    path('editar/<int:pk>', EditarProjeto.as_view() , name='update'),
    path('delete/<int:pk>', DeletarProjeto.as_view() , name='delete'),
    # path('', TemplateView.as_view(template_name='index.html'), name='home'),
]