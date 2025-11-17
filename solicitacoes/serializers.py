from rest_framework import serializers
from .models import Solicitacao
from django.contrib.auth import get_user_model
User = get_user_model()

class SolicitacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitacao
        fields = '__all__'
        read_only_fields = ['usuario']

    def create(self, validated_data):
        validated_data['usuario'] = User.objects.get(id=1)
        return super().create(validated_data)
