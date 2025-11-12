from rest_framework import serializers
from .models import Manutencao

class ManutencaoSerializer(serializers.ModelSerializer):
    patrimonio_nome = serializers.ReadOnlyField(source='patrimonio.nome')

    class Meta:
        model = Manutencao
        fields = '__all__'
