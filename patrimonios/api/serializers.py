from rest_framework import serializers
from patrimonios.models import EspacoFisico, Patrimonio

class EspacoFisicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EspacoFisico
        fields = '__all__'
