from django.contrib import admin
from .models import Solicitacao

@admin.register(Solicitacao)
class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'patrimonio', 'tipo', 'status', 'data_registro')
    search_fields = ('usuario__username', 'patrimonio__nome', 'descricao')
    list_filter = ('status', 'tipo')
