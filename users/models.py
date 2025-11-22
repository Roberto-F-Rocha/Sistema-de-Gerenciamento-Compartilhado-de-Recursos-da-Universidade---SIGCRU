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
        """
        Garante que somente admins tenham acesso ao Django Admin.
        """
        if self.tipo_usuario == "admin":
            self.is_staff = True
            self.is_superuser = True
        else:
            # Garante segurança do sistema
            self.is_staff = False
            self.is_superuser = False

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.get_tipo_usuario_display() if self.tipo_usuario else 'Sem tipo'})"
