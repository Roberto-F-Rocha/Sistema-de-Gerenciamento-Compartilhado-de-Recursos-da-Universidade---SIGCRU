from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Solicitacao

def listar_solicitacoes(user: User):
    if user.is_staff:
        return Solicitacao.objects.all()
    return Solicitacao.objects.filter(usuario=user)

def obter_solicitacao(solicitacao_id: int, user: User):
    solicitacao = get_object_or_404(Solicitacao, id=solicitacao_id)

    if not user.is_staff and solicitacao.usuario != user:
        raise PermissionError("Você não tem permissão para acessar esta solicitação.")

    return solicitacao

def criar_solicitacao(validated_data, user: User):
    return Solicitacao.objects.create(usuario=user, **validated_data)

def atualizar_solicitacao(solicitacao: Solicitacao, validated_data, user: User):
    if not user.is_staff and solicitacao.usuario != user:
        raise PermissionError("Você não pode editar esta solicitação.")

    for campo, valor in validated_data.items():
        setattr(solicitacao, campo, valor)

    solicitacao.save()
    return solicitacao

def deletar_solicitacao(solicitacao: Solicitacao, user: User):
    if not user.is_staff and solicitacao.usuario != user:
        raise PermissionError("Você não pode deletar esta solicitação.")

    solicitacao.delete()
    return True