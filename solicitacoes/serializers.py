from rest_framework import serializers
from .models import Solicitacao

class SolicitacaoSerializer(serializers.ModelSerializer):
    patrimonio_nome = serializers.CharField(
        source='patrimonio.nome',
        read_only=True
    )

    # adiciona sala + bloco da localização
    localizacao_sala = serializers.CharField(
        source='patrimonio.localizacao.nome',
        read_only=True
    )
    localizacao_bloco = serializers.CharField(
        source='patrimonio.localizacao.bloco',
        read_only=True
    )

    class Meta:
        model = Solicitacao
        fields = '__all__'
        read_only_fields = ['usuario', 'patrimonio_nome', 'localizacao_sala', 'localizacao_bloco']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['usuario'] = request.user
        return super().create(validated_data)
