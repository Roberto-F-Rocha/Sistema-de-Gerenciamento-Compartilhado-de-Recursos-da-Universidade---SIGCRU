from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from patrimonios.models import EspacoFisico

def listar_espacos_fisicos():
    return EspacoFisico.objects.all()

def obter_espaco_fisico(espaco_id: int):
    return get_object_or_404(EspacoFisico, id=espaco_id)

def criar_espaco_fisico(validated_data):
    try:
        return EspacoFisico.objects.create(**validated_data)
    except IntegrityError:
        raise ValueError("Já existe um espaço físico com este nome.")

def atualizar_espaco_fisico(espaco: EspacoFisico, validated_data):
    for campo, valor in validated_data.items():
        setattr(espaco, campo, valor)
    try:
        espaco.save()
    except IntegrityError:
        raise ValueError("Já existe um espaço físico com este nome.")
    return espaco

def deletar_espaco_fisico(espaco: EspacoFisico):
    espaco.delete()
    return True
