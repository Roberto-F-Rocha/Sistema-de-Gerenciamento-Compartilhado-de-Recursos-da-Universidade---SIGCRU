from rest_framework import viewsets, permissions
from .models import Solicitacao
from .serializers import SolicitacaoSerializer

class SolicitacaoViewSet(viewsets.ModelViewSet):
    queryset = Solicitacao.objects.all()
    serializer_class = SolicitacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Solicitacao.objects.all()
        return Solicitacao.objects.filter(usuario=user)
    
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
