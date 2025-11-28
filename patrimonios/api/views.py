from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from patrimonios.models import EspacoFisico
from .serializers import EspacoFisicoSerializer
from .services import (
    listar_espacos_fisicos,
    obter_espaco_fisico,
    criar_espaco_fisico,
    atualizar_espaco_fisico,
    deletar_espaco_fisico,
)

class EspacoFisicoViewSet(viewsets.ModelViewSet):
    queryset = EspacoFisico.objects.all()
    serializer_class = EspacoFisicoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return listar_espacos_fisicos()

    def perform_create(self, serializer):
        return criar_espaco_fisico(serializer.validated_data)

    def perform_update(self, serializer):
        espaco = obter_espaco_fisico(self.kwargs["pk"])
        return atualizar_espaco_fisico(espaco, serializer.validated_data)

    def perform_destroy(self, instance):
        return deletar_espaco_fisico(instance)
