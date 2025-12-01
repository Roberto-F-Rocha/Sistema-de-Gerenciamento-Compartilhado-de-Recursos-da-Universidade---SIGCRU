from django.db import models
from django.conf import settings
from patrimonios.models import Patrimonio
from django.utils import timezone

class Solicitacao(models.Model):
    TIPOS = [
        ('falta', 'Falta'),
        ('dano', 'Dano'),
        ('manutencao', 'Manutenção'),
        ('substituicao', 'Substituição'),
    ]

    titulo = models.CharField(max_length=255, default= "Sem título")

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    patrimonio = models.ForeignKey(
        Patrimonio,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    tipo = models.CharField(max_length=20, choices=TIPOS)
    descricao = models.TextField()
    data_registro = models.DateTimeField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=[
            ('aberto', 'Aberto'),
            ('em_analise', 'Em análise'),
            ('resolvido', 'Resolvido'),
            ('cancelado', 'Cancelado'),
        ],
        default='aberto'
    )

    data_criacao = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.titulo} - {self.tipo} ({self.usuario})"

    class Meta:
        permissions = [
            ("create_solicitacao", "Pode criar solicitação"),
            ("approve_solicitacao", "Pode aprovar solicitação"),
        ]
