from rest_framework import serializers
from patrimonios.models import Patrimonio, Localizacao

class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacao
        fields = ['id', 'nome']

class EspacoFisicoSerializer(serializers.ModelSerializer):
    localizacao_nome = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Patrimonio
        fields = '__all__'

    def create(self, validated_data):
        loc_nome = validated_data.pop("localizacao_nome", None)
        if loc_nome:
            loc, _ = Localizacao.objects.get_or_create(nome=loc_nome)
            validated_data["localizacao"] = loc
        return super().create(validated_data)

    def update(self, instance, validated_data):
        loc_nome = validated_data.pop("localizacao_nome", None)
        if loc_nome:
            loc, _ = Localizacao.objects.get_or_create(nome=loc_nome)
            validated_data["localizacao"] = loc
        return super().update(instance, validated_data)
