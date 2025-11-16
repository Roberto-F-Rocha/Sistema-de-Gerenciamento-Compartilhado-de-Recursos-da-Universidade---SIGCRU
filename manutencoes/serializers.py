from rest_framework import serializers
from .models import Manutencao

class ManutencaoSerializer(serializers.ModelSerializer):
    patrimonio_nome = serializers.ReadOnlyField(source='patrimonio.nome')

    class Meta:
        model = Manutencao
        fields = '__all__'

    def validate(self, attrs):
        status = attrs.get("status", getattr(self.instance, "status", None))
        data_fim = attrs.get("data_fim")

        # Se status != concluída, data_fim NÃO pode ser enviada
        if status != "concluida" and data_fim is not None:
            raise serializers.ValidationError({
                "data_fim": "Só é permitido informar a data_fim quando o status for 'concluida'."
            })

        # Se status = concluída, data_fim é obrigatória
        if status == "concluida" and data_fim is None:
            raise serializers.ValidationError({
                "data_fim": "Quando a manutenção for concluída, é obrigatório informar a data_fim."
            })

        return attrs
