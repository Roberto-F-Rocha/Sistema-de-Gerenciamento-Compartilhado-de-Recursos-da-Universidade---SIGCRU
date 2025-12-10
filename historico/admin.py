from django.contrib import admin
from .models import HistoricoAtividade


@admin.register(HistoricoAtividade)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nome_item",
        "numero_tombo",
        "localizacao_formatada",
        "status",
        "tipo",
        "data_abertura",
        "data_atualizacao",
    )

    search_fields = (
        "nome_item",
        "numero_tombo",
        "localizacao_fk__nome",
        "localizacao_fk__bloco",
        "status",
    )

    list_filter = ("tipo", "status")

    readonly_fields = (
        "id",
        "nome_item",
        "numero_tombo",
        "localizacao_formatada",
        "status",
        "tipo",
        "data_abertura",
        "data_atualizacao",
        "criado_em",
    )

    # Não permitir adicionar
    def has_add_permission(self, request):
        return False
