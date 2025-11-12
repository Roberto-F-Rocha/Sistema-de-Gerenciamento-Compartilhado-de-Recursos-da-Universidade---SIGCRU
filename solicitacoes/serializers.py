from rest_framework import serializers
from .models import Solicitacao

class SolicitacaoSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.ReadOnlyField(source='usuario.username')
    patrimonio_nome = serializers.ReadOnlyField(source='patrimonio.nome')

    class Meta:
        model = Solicitacao
        fields = '__all__'
