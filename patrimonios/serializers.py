from rest_framework import serializers
from .models import Patrimonio, Localizacao

class PatrimonioSerializer(serializers.ModelSerializer):
    # permite criar nova localização digitando
    localizacao_nome = serializers.CharField(write_only=True, required=False)
    localizacao_bloco = serializers.CharField(write_only=True, required=False)
    localizacao_tipo = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Patrimonio
        fields = '__all__'

    def create(self, validated_data):
        loc_nome = validated_data.pop("localizacao_nome", None)
        loc_bloco = validated_data.pop("localizacao_bloco", None)
        loc_tipo = validated_data.pop("localizacao_tipo", None)

        if loc_nome:
            loc, _ = Localizacao.objects.get_or_create(nome=loc_nome)
            validated_data["localizacao"] = loc
            
        if loc_bloco:
            loc, _ = Localizacao.objects.get_or_create(bloco=loc_bloco)
            validated_data["localizacao"] = loc
        
        if loc_tipo:
            loc, _ = Localizacao.objects.get_or_create(tipo=loc_tipo)
            validated_data["localizacao"] = loc

        return super().create(validated_data)

    def update(self, instance, validated_data):
        loc_nome = validated_data.pop("localizacao_nome", None)
        loc_bloco = validated_data.pop("localizacao_bloco", None)
        loc_tipo = validated_data.pop("localizacao_tipo", None)

        if loc_nome:
            loc, _ = Localizacao.objects.get_or_create(nome=loc_nome)
            validated_data["localizacao"] = loc
        
        if loc_bloco:
            loc, _ = Localizacao.objects.get_or_create(bloco=loc_bloco)
            validated_data["localizacao"] = loc
        
        if loc_tipo:
            loc, _ = Localizacao.objects.get_or_create(tipo=loc_tipo)
            validated_data["localizacao"] = loc

        return super().update(instance, validated_data)