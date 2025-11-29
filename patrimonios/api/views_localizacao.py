from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from patrimonios.models import Localizacao
from .serializers_localizacao import LocalizacaoSerializer
from .services_localizacao import (
    listar_localizacoes,
    obter_localizacao,
    criar_localizacao,
    atualizar_localizacao,
    deletar_localizacao,
)


class LocalizacaoViewSet(viewsets.ModelViewSet):
    serializer_class = LocalizacaoSerializer
    queryset = Localizacao.objects.all()
    permission_classes = [AllowAny]

    def get_queryset(self):
        return listar_localizacoes()

    def perform_create(self, serializer):
        criar_localizacao(serializer.validated_data)

    def perform_update(self, serializer):
        local = obter_localizacao(self.kwargs["pk"])
        atualizar_localizacao(local, serializer.validated_data)

    def perform_destroy(self, instance):
        deletar_localizacao(instance)
