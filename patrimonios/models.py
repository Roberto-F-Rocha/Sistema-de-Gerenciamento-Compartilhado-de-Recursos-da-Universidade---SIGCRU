from django.db import models
from django.contrib.auth.models import User

class Patrimonio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    numero_tombo = models.CharField(max_length=50, unique=True)
    localizacao = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[
            ('ativo', 'Ativo'),
            ('em_manutencao', 'Em manutenção'),
            ('inativo', 'Inativo')
        ],
        default='ativo'
    )
    responsavel = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    data_aquisicao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.numero_tombo})"
