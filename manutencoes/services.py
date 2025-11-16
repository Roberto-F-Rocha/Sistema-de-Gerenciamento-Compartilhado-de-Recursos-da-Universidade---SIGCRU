from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.db import transaction
from .models import Manutencao
from patrimonios.models import Patrimonio


class ManutencaoService:

    @staticmethod
    def listar_manutencoes():
        return Manutencao.objects.all().select_related('patrimonio', 'usuario')

    @staticmethod
    def detalhar_manutencao(manutencao_id: int):
    
        return get_object_or_404(
            Manutencao.objects.select_related('patrimonio', 'usuario'),
            id=manutencao_id
        )

    @staticmethod
    @transaction.atomic
    def criar_manutencao(validated_data: dict, usuario: User):
    
        patrimonio_id = validated_data.get("patrimonio").id

        patrimonio = get_object_or_404(Patrimonio, id=patrimonio_id)

        manutencao = Manutencao.objects.create(
            patrimonio=patrimonio,
            usuario=usuario,
            descricao=validated_data.get("descricao"),
            data_inicio=validated_data.get("data_inicio"),  # AGORA VEM DO FRONT
            data_fim=validated_data.get("data_fim"),
            status=validated_data.get("status", "pendente"),
        )

        return manutencao

    @staticmethod
    @transaction.atomic
    def atualizar_manutencao(manutencao_id: int, validated_data: dict):
    
        manutencao = get_object_or_404(Manutencao, id=manutencao_id)

        
        for field, value in validated_data.items():
            setattr(manutencao, field, value)

        manutencao.save()
        return manutencao

    @staticmethod
    @transaction.atomic
    def deletar_manutencao(manutencao_id: int):

        manutencao = get_object_or_404(Manutencao, id=manutencao_id)
        manutencao.delete()
        return True
