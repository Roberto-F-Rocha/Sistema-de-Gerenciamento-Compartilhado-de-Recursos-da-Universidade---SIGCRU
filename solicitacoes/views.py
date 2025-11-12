from rest_framework import viewsets, permissions
from .models import Solicitacao
from .serializers import SolicitacaoSerializer

class SolicitacaoViewSet(viewsets.ModelViewSet):
    queryset = Solicitacao.objects.all().select_related('usuario', 'patrimonio')
    serializer_class = SolicitacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
