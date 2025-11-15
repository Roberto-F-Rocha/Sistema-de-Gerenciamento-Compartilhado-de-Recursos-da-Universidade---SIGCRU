from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import Patrimonio
from .serializers import PatrimonioSerializer

class PatrimonioViewSet(viewsets.ModelViewSet):
    queryset = Patrimonio.objects.all()
    serializer_class = PatrimonioSerializer

        # Permite criar itens sem autenticação
    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        return super().get_permissions()