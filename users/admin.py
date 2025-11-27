from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "email", "tipo_usuario", "is_active", "is_staff")
    list_filter = ("tipo_usuario", "is_staff", "is_superuser")
    fieldsets = UserAdmin.fieldsets + (
        ("Informações Institucionais", {"fields": ("matricula", "tipo_usuario")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Informações Institucionais", {"fields": ("matricula", "tipo_usuario")}),
    )
    search_fields = ("username", "email", "matricula")
