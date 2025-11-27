from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from patrimonios.models import Patrimonio, Localizacao

# --- Espaços físicos ---
def listar_espacos_fisicos():
    return Patrimonio.objects.all()

def obter_espaco_fisico(espaco_id: int):
    return get_object_or_404(Patrimonio, id=espaco_id)

def criar_espaco_fisico(validated_data):
    try:
        return Patrimonio.objects.create(**validated_data)
    except IntegrityError:
        raise ValueError("Já existe um espaço físico com este número de tombo.")

def atualizar_espaco_fisico(espaco: Patrimonio, validated_data):
    for campo, valor in validated_data.items():
        setattr(espaco, campo, valor)
    try:
        espaco.save()
    except IntegrityError:
        raise ValueError("Já existe um espaço físico com este número de tombo.")
    return espaco

def deletar_espaco_fisico(espaco: Patrimonio):
    espaco.delete()
    return True

# --- Localizações ---
def listar_localizacoes():
    return Localizacao.objects.all()
