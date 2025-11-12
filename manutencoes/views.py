from rest_framework import viewsets, permissions
from .models import Manutencao
from .serializers import ManutencaoSerializer

class ManutencaoViewSet(viewsets.ModelViewSet):
    queryset = Manutencao.objects.all().select_related('patrimonio', 'usuario')
    serializer_class = ManutencaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
