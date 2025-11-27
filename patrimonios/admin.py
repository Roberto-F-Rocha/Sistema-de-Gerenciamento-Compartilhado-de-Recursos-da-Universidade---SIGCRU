from django.contrib import admin
from .models import Patrimonio, EspacoFisico

@admin.register(Patrimonio)
class PatrimonioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'numero_tombo', 'status', 'responsavel', 'data_aquisicao')
    search_fields = ('nome', 'numero_tombo', 'descricao')
    list_filter = ('status',)
    
@admin.register(EspacoFisico)
class EspacoFisicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'tipo', 'responsavel')
    search_fields = ('nome', 'tipo')
    list_filter = ('tipo',)
    filter_horizontal = ('recursos',)