from turtle import update
from django.db import models
from allauth import app_settings as allauth_app_settings

    # declare a new model with a name "GeeksModel"
class ProjetosModel(models.Model):
 
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField(verbose_name=("Descrição"))
        
    def __str__(self):
        return self.title
    
class Tarefas(models.Model):
 
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
    id_user = models.ForeignKey(
        allauth_app_settings.USER_MODEL,
        verbose_name=("user"),
        on_delete=models.CASCADE,
    )
    id_projeto = models.ForeignKey(ProjetosModel,
        on_delete=models.CASCADE,
    )
    data_inicio = models.DateTimeField()
    data_final = models.DateTimeField()
    status = models.CharField(max_length=200)
    se_ativo =models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
        
class Check_list_tarefas(models.Model):
 
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
    id_user = models.ForeignKey(
        allauth_app_settings.USER_MODEL,
        verbose_name=("user"),
        on_delete=models.CASCADE,
    )
    id_tarefas = models.ForeignKey(Tarefas,
        on_delete=models.CASCADE,
    )
    data_final = models.DateTimeField()
    status = models.CharField(max_length=200)
    se_ativo =models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title