from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import Patrimonio
from .serializers import PatrimonioSerializer

from .services import (
    listar_patrimonios,
    obter_patrimonio,
    criar_patrimonio,
    atualizar_patrimonio,
    deletar_patrimonio,
)


class PatrimonioViewSet(viewsets.ModelViewSet):
    serializer_class = PatrimonioSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        return super().get_permissions()

    def get_queryset(self):
        return listar_patrimonios()

    def perform_create(self, serializer):
        criar_patrimonio(serializer.validated_data)

    def perform_update(self, serializer):
        patrimonio = obter_patrimonio(self.kwargs["pk"])
        atualizar_patrimonio(patrimonio, serializer.validated_data)

    def perform_destroy(self, instance):
        deletar_patrimonio(instance)
