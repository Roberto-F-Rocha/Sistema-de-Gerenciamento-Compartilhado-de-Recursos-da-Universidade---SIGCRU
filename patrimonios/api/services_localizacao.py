from django.shortcuts import get_object_or_404
from patrimonios.models import Localizacao


def listar_localizacoes():
    return Localizacao.objects.all()


def obter_localizacao(localizacao_id):
    return get_object_or_404(Localizacao, id=localizacao_id)


def criar_localizacao(data):
    return Localizacao.objects.create(**data)


def atualizar_localizacao(localizacao, data):
    for campo, valor in data.items():
        setattr(localizacao, campo, valor)
    localizacao.save()
    return localizacao


def deletar_localizacao(localizacao):
    localizacao.delete()
