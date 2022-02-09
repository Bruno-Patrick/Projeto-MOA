from django.db import models

class Clientes(models.Model):
    nome = models.CharField('Digite seu nome', max_length=200)
    email = models.CharField('Digite seu email', max_length=200)
    telefone = models.CharField('Digite seu telefone', max_length=200)
       
    def __str__(self):
        return self.nome