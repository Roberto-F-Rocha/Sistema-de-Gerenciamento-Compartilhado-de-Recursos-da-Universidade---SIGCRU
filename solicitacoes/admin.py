from django.contrib import admin
from .models import Solicitacao

@admin.register(Solicitacao)
class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'patrimonio', 'tipo', 'status', 'data_registro')
    search_fields = ('usuario__username', 'patrimonio__nome', 'descricao')
    list_filter = ('status', 'tipo')

    # remove campos automáticos do formulário
    readonly_fields = ('data_registro', 'data_criacao')

    # controla os campos exibidos na página de edição
    def get_fields(self, request, obj=None):
        return (
            'usuario',
            'patrimonio',
            'tipo',
            'descricao',
            'status',
        )
