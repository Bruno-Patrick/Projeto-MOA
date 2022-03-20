from pipes import Template
from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', CriarProjeto.as_view()),
]