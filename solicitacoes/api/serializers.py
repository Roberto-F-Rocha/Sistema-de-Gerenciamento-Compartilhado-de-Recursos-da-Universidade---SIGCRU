from rest_framework import serializers
from solicitacoes.models import Solicitacao

class SolicitacaoSerializer(serializers.ModelSerializer):
    patrimonio_nome = serializers.CharField(source="patrimonio.nome", read_only=True)

    class Meta:
        model = Solicitacao
        fields = [
            "id",
            "patrimonio",
            "patrimonio_nome",
            "descricao",
            "status",
            "criado_em",
            "atualizado_em",
        ]
        read_only_fields = ["status", "criado_em", "atualizado_em"]
