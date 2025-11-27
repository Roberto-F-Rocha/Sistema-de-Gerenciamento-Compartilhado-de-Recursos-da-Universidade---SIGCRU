from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        from django.contrib.auth.models import Group, Permission

        grupos = ["aluno", "professor", "servidor", "admin"]
        for g in grupos:
            Group.objects.get_or_create(name=g)

        permissoes_por_grupo = {
            "aluno": [],
            "professor": [],
            "servidor": [
                "add_patrimonio",
                "change_patrimonio",
                "delete_patrimonio",
                "view_patrimonio",
                "add_solicitacao",
                "change_solicitacao",
                "add_manutencao",
            ],
            "admin": "__all__",
        }

        for nome_grupo, perms in permissoes_por_grupo.items():
            group = Group.objects.get(name=nome_grupo)

            if perms == "__all__":
                group.permissions.set(Permission.objects.all())
                continue

            permissoes = []
            for codename in perms:
                try:
                    permissoes.append(Permission.objects.get(codename=codename))
                except Permission.DoesNotExist:
                    continue

            group.permissions.set(permissoes)
