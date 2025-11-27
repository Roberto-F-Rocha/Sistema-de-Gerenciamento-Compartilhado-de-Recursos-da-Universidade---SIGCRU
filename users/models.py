from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    TIPO_USUARIO_CHOICES = [
        ("aluno", "Aluno"),
        ("professor", "Professor"),
        ("servidor", "Servidor"),
        ("admin", "Administrador"),
    ]

    matricula = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        blank=True,
        help_text="Matrícula SIGAA ou SIAPE/CIAPE"
    )

    tipo_usuario = models.CharField(
        max_length=20,
        choices=TIPO_USUARIO_CHOICES,
        null=True,
        blank=True,
        help_text="Define o perfil institucional"
    )

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.is_staff = True
        elif self.tipo_usuario == "admin":
            # admin institucional: acesso ao admin, mas não superuser
            self.is_staff = True
        else:
            self.is_staff = False

        super().save(*args, **kwargs)

    def __str__(self):
        tipo = self.get_tipo_usuario_display() if self.tipo_usuario else "Sem tipo"
        return f"{self.username} ({tipo})"
