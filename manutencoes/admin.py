from django.contrib import admin
from .models import Manutencao

@admin.register(Manutencao)
class ManutencaoAdmin(admin.ModelAdmin):
    list_display = ('id', 'patrimonio', 'usuario', 'status', 'data_inicio', 'data_fim')
    search_fields = ('patrimonio__nome', 'descricao', 'usuario__username')

    def get_fieldsets(self, request, obj=None):
        fieldsets = [
            (None, {
                "fields": ("patrimonio", "usuario", "descricao", "status")
            }),
        ]

        data_fields = ["data_inicio"]
        
        # Apenas exibe 'data_fim' se o status já for 'concluida'
        if obj and obj.status == "concluida":
            data_fields.append("data_fim")
        
        fieldsets.append(("Datas", {
            "fields": tuple(data_fields),
        }))
        
        return fieldsets

    def save_model(self, request, obj, form, change):
        # Se o status for alterado para algo diferente de 'concluida',
        # a data de fim deve ser zerada.
        if obj.status != "concluido":
            obj.data_fim = None
            
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        return ()