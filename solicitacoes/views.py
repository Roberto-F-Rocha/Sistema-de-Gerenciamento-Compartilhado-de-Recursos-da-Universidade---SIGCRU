from rest_framework import viewsets, permissions, generics
from .models import Solicitacao
from .serializers import SolicitacaoSerializer

from .services import (
    listar_solicitacoes,
    obter_solicitacao,
    criar_solicitacao,
    atualizar_solicitacao,
    deletar_solicitacao,
)

class SolicitacaoViewSet(viewsets.ModelViewSet):
    serializer_class = SolicitacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return listar_solicitacoes(self.request.user)

    def perform_create(self, serializer):
        criar_solicitacao(serializer.validated_data, self.request.user)

    def perform_update(self, serializer):
        solicitacao = obter_solicitacao(self.kwargs["pk"], self.request.user)
        atualizar_solicitacao(solicitacao, serializer.validated_data, self.request.user)

    def perform_destroy(self, instance):
        deletar_solicitacao(instance, self.request.user)

class MinhasSolicitacoesView(generics.ListAPIView):
    serializer_class = SolicitacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Solicitacao.objects.filter(usuario=self.request.user).order_by("-data_criacao")
