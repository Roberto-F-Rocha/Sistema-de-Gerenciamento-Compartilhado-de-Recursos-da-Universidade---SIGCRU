from rest_framework import viewsets, permissions
from .models import Solicitacao
from .serializers import SolicitacaoSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

from .services import (
    listar_solicitacoes,
    obter_solicitacao,
    criar_solicitacao,
    atualizar_solicitacao,
    deletar_solicitacao,
)

class SolicitacaoViewSet(viewsets.ModelViewSet):
    serializer_class = SolicitacaoSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return listar_solicitacoes(User.objects.get(id=1))

    def perform_create(self, serializer):
        criar_solicitacao(serializer.validated_data, User.objects.get(id=1))

    def perform_update(self, serializer):
        solicitacao = obter_solicitacao(self.kwargs["pk"], User.objects.get(id=1))
        atualizar_solicitacao(solicitacao, serializer.validated_data, User.objects.get(id=1))

    def perform_destroy(self, instance):
        deletar_solicitacao(instance, User.objects.get(id=1))
