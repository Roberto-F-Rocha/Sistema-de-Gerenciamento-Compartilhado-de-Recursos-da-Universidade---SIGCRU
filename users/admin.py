from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    #Campos exibidos na listagem
    list_display = ("username", "email", "tipo_usuario", "is_active")
    list_filter = ("tipo_usuario", "is_active")

    #campos aparecem ao editar um usuário
    fieldsets = (
        ("Dados de Login", {"fields": ("username", "password")}),
        ("Informações Pessoais", {"fields": ("first_name", "last_name", "email", "matricula")}),
        ("Perfil Institucional", {"fields": ("tipo_usuario",)}),
        ("Permissões", {"fields": ("is_active", "groups", "user_permissions")}),
        ("Datas Importantes", {"fields": ("last_login", "date_joined")}),
    )

    #Campos ao criar um novo usuário via admin
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "tipo_usuario", "matricula"),
        }),
    )

    search_fields = ("username", "email", "matricula")
    ordering = ("username",)
