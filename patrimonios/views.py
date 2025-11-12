from rest_framework import viewsets, permissions
from .models import Patrimonio
from .serializers import PatrimonioSerializer

class PatrimonioViewSet(viewsets.ModelViewSet):
    queryset = Patrimonio.objects.all()
    serializer_class = PatrimonioSerializer
    permission_classes = [permissions.IsAuthenticated]
