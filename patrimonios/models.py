from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Localizacao(models.Model):
    nome = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.nome


class Patrimonio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    numero_tombo = models.CharField(max_length=50, unique=True)

    # ALTERAÇÃO: agora é FK, mas mantendo o nome original
    localizacao = models.ForeignKey(
        Localizacao,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=[
            ('ativo', 'Ativo'),
            ('em_manutencao', 'Em manutenção'),
            ('inativo', 'Inativo')
        ],
        default='ativo'
    )
    responsavel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    data_aquisicao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} ({self.numero_tombo})"
