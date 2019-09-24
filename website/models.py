from django.db import models
from django.utils import timezone

class Pessoas(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    sobrenome = models.CharField(max_length=255, verbose_name='Sobrenome')
    data_de_nascimento = models.DateField(verbose_name='Data de nascimento')
    cpf = models.CharField(max_length= 14, verbose_name='CPF')
    cep = models.CharField(max_length= 10, verbose_name='CEP')
    item_de_doacao = models.CharField(max_length=255, verbose_name='Item de doação')
    ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name='Data de criação')
