from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from patrimonios.models import Patrimonio, Localizacao
from .serializers import EspacoFisicoSerializer, LocalizacaoSerializer
from .services import (
    listar_espacos_fisicos,
    obter_espaco_fisico,
    criar_espaco_fisico,
    atualizar_espaco_fisico,
    deletar_espaco_fisico,
    listar_localizacoes
)
from rest_framework.decorators import action
from rest_framework.response import Response

class EspacoFisicoViewSet(viewsets.ModelViewSet):
    serializer_class = EspacoFisicoSerializer
    queryset = Patrimonio.objects.all()

    def get_permissions(self):
        if self.request.method == "POST":
            return [IsAuthenticated()]
        return super().get_permissions()

    def get_queryset(self):
        return listar_espacos_fisicos()

    def perform_create(self, serializer):
        criar_espaco_fisico(serializer.validated_data)

    def perform_update(self, serializer):
        espaco = obter_espaco_fisico(self.kwargs["pk"])
        atualizar_espaco_fisico(espaco, serializer.validated_data)

    def perform_destroy(self, instance):
        deletar_espaco_fisico(instance)

class LocalizacaoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LocalizacaoSerializer
    queryset = Localizacao.objects.all()

    @action(detail=False, methods=["get"], permission_classes=[AllowAny])
    def listar(self, request):
        locais = listar_localizacoes()
        serializer = self.get_serializer(locais, many=True)
        return Response(serializer.data)
