from django.contrib import admin
from .models import Patrimonio, Localizacao


@admin.register(Localizacao)
class LocalizacaoAdmin(admin.ModelAdmin):
    search_fields = ("nome",)


@admin.register(Patrimonio)
class PatrimonioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'numero_tombo', 'localizacao', 'status', 'responsavel', 'data_aquisicao')
    search_fields = ('nome', 'numero_tombo', 'descricao', 'localizacao__nome')
    list_filter = ('status', 'localizacao')
    autocomplete_fields = ('localizacao',)
