from rest_framework import viewsets, permissions, generics
from .models import Solicitacao
from .serializers import SolicitacaoSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

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

    @action(detail=False, methods=["get"], url_path="minhas")
    def minhas(self, request):
        qs = Solicitacao.objects.filter(usuario=request.user).order_by("-data_criacao")
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

