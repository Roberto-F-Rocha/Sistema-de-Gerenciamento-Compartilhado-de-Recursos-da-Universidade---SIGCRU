from django.contrib import admin
from .models import Manutencao

@admin.register(Manutencao)
class ManutencaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'patrimonio', 'usuario', 'status', 'data_inicio', 'data_fim')
    search_fields = ('patrimonio__nome', 'descricao', 'usuario__username')
    list
