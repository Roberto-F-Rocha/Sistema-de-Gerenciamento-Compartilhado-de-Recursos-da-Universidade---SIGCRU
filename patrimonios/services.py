from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from .models import Patrimonio


def listar_patrimonios():
    return Patrimonio.objects.all()


def obter_patrimonio(patrimonio_id: int):
    return get_object_or_404(Patrimonio, id=patrimonio_id)


def criar_patrimonio(validated_data):
    try:
        return Patrimonio.objects.create(**validated_data)
    except IntegrityError:
        raise ValueError("Já existe um patrimônio com este número de tombo.")


def atualizar_patrimonio(patrimonio: Patrimonio, validated_data):
    for campo, valor in validated_data.items():
        setattr(patrimonio, campo, valor)

    try:
        patrimonio.save()
    except IntegrityError:
        raise ValueError("Já existe um patrimônio com este número de tombo.")

    return patrimonio


def deletar_patrimonio(patrimonio: Patrimonio):
    patrimonio.delete()
    return True