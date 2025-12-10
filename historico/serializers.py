from rest_framework import serializers
from .models import HistoricoAtividade

class HistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoAtividade
        fields = '__all__'
