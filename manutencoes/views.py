from rest_framework import viewsets, permissions
from .serializers import ManutencaoSerializer
from .models import Manutencao
from .services import ManutencaoService


class ManutencaoViewSet(viewsets.ModelViewSet):
    serializer_class = ManutencaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ManutencaoService.listar_manutencoes()

    def perform_create(self, serializer):
        ManutencaoService.criar_manutencao(serializer.validated_data, self.request.user)

    def perform_update(self, serializer):
        ManutencaoService.atualizar_manutencao(self.kwargs["pk"], serializer.validated_data)

    def perform_destroy(self, instance):
        ManutencaoService.deletar_manutencao(self.kwargs["pk"])
