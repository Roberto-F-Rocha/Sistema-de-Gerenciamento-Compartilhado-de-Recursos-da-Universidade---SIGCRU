from django.db.models.signals import post_save
from django.dispatch import receiver

from solicitacoes.models import Solicitacao
from manutencoes.models import Manutencao
from .models import HistoricoAtividade


def formatar_localizacao(localizacao):
    if not localizacao:
        return None

    if hasattr(localizacao, "nome"):
        bloco = f" - {localizacao.bloco}" if localizacao.bloco else ""
        return f"{localizacao.nome}{bloco}"

    return localizacao


@receiver(post_save, sender=Solicitacao)
def historico_solicitacao(sender, instance, created, **kwargs):
    patrimonio = instance.patrimonio

    HistoricoAtividade.objects.create(
        tipo="solicitacao",
        item_id=instance.id,
        nome_item=instance.titulo,
        numero_tombo=patrimonio.numero_tombo if patrimonio else None,
        localizacao=formatar_localizacao(patrimonio.localizacao) if patrimonio else None,
        status=instance.status,
        data_abertura=instance.data_registro,
        data_atualizacao=instance.data_criacao,
    )


@receiver(post_save, sender=Manutencao)
def historico_manutencao(sender, instance, created, **kwargs):
    patrimonio = instance.patrimonio

    HistoricoAtividade.objects.create(
        tipo="manutencao",
        item_id=instance.id,
        nome_item=patrimonio.nome if patrimonio else None,
        numero_tombo=patrimonio.numero_tombo if patrimonio else None,
        localizacao=formatar_localizacao(patrimonio.localizacao) if patrimonio else None,
        status=instance.status,
        data_abertura=instance.data_inicio,
        data_atualizacao=instance.data_fim or instance.data_inicio,
    )
