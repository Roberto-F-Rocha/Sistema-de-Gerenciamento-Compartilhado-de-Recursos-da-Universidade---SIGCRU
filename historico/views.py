from rest_framework import viewsets, permissions
from .models import HistoricoAtividade
from .serializers import HistoricoSerializer


class HistoricoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HistoricoAtividade.objects.all().order_by('-criado_em')
    serializer_class = HistoricoSerializer
    permission_classes = [permissions.IsAdminUser]  # APENAS ADM
