from django.db import models
from django.conf import settings
from patrimonios.models import Localizacao


class HistoricoAtividade(models.Model):
    TIPOS = [
        ("solicitacao", "Solicitação"),
        ("manutencao", "Manutenção"),
    ]

    usuario_acao = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL,
        related_name="historico_acoes"
    )

    tipo = models.CharField(max_length=20, choices=TIPOS)
    item_id = models.IntegerField()
    nome_item = models.CharField(max_length=255)
    numero_tombo = models.CharField(max_length=100, null=True, blank=True)

    localizacao_fk = models.ForeignKey(
        Localizacao,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="historicos"
    )

    localizacao = models.CharField(max_length=255, null=True, blank=True)

    status = models.CharField(max_length=50)
    data_abertura = models.DateTimeField()
    data_atualizacao = models.DateTimeField()

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} #{self.item_id} - {self.status}"

    @property
    def localizacao_formatada(self):
        if self.localizacao_fk:
            nome = self.localizacao_fk.nome
            bloco = self.localizacao_fk.bloco

            if bloco:
                return f"{nome} - {bloco}"
            return nome

        return self.localizacao or ""
