from django import forms
from .models import ProjetosModel
from django.views.generic.detail import DetailView
 
 
# creating a form

class ProjetosForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = ProjetosModel
        # specify fields to be use
        fields = [
            'title',
            'description',
        ]