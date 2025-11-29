from rest_framework import serializers
from patrimonios.models import Localizacao

class LocalizacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localizacao
        fields = "__all__"
