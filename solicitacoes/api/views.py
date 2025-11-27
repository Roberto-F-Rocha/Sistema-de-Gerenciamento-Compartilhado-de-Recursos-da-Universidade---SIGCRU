from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from solicitacoes.models import Solicitacao
from .serializers import SolicitacaoSerializer

class MinhasSolicitacoesView(generics.ListAPIView):
    serializer_class = SolicitacaoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # Admin e servidor visualizam tudo
        if user.tipo_usuario in ["admin", "servidor"]:
            return Solicitacao.objects.all()

        # Usuário comum visualiza apenas as próprias
        return Solicitacao.objects.filter(usuario=user)
