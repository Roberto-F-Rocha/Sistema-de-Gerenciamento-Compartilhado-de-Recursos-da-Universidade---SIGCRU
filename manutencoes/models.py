from django.db import models
from django.contrib.auth.models import User
from patrimonios.models import Patrimonio
from django.conf import settings

class Manutencao(models.Model):
    patrimonio = models.ForeignKey(Patrimonio, on_delete=models.CASCADE, related_name='manutencoes')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    descricao = models.TextField()
    
    # AGORA É MANUAL removido auto_now_add
    data_inicio = models.DateField()

    # só preenchido quando concluída
    data_fim = models.DateField(null=True, blank=True)

    status = models.CharField(
        max_length=20,
        choices=[
            ('pendente', 'Pendente'),
            ('em_andamento', 'Em andamento'),
            ('concluido', 'Concluido')
        ],
        default='pendente'
    )

    def __str__(self):
        return f"Manutenção de {self.patrimonio.nome} - {self.status}"
    
    
    class Meta:
        permissions = [
            ("create_manutencao", "Pode criar manutenção"),
        ]

        def __str__(self):
            return f"Manutenção #{self.pk}"
