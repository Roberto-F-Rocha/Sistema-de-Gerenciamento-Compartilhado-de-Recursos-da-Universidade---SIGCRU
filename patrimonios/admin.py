from django.contrib import admin
from .models import Patrimonio

@admin.register(Patrimonio)
class PatrimonioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'numero_tombo', 'localizacao', 'status', 'responsavel', 'data_aquisicao')
    search_fields = ('nome', 'numero_tombo', 'descricao', 'localizacao')
    list_filter = ('status', 'localizacao')
