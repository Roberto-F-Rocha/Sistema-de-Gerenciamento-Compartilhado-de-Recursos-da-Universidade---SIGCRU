from django.db import migrations

LOCALIZACOES_PADRAO = [
    "Administrativo - Auditório Administrativo",
    "Administrativo - Sala de reuniões",
    "Central de Aulas I - Sala de aula 01",
    "Central de Aulas I - Sala de aula 02",
    "Central de Aulas I - Sala de aula 03",
    "Central de Aulas I - Sala de aula 04",
    "Central de Aulas I - Sala de aula 05",
    "Central de Aulas I - Sala de aula 06",
    "Central de Aulas I - Sala de aula 07",
    "Central de Aulas I - Sala de aula 08",
    "Central de Aulas I - Sala de aula 09",
    "Central de Aulas I - Sala de aula 10",
    "Central de Aulas II - Ateliê de Desenho I",
    "Central de Aulas II - Ateliê de Desenho II",
    "Central de Aulas II - Laboratório de Informática 01 (IMD)",
    "Central de Aulas II - Laboratório de Informática 02 (IMD)",
    "Central de Aulas II - Sala de aula 01",
    "Central de Aulas II - Sala de aula 02",
    "Central de Aulas II - Sala de aula 03",
    "Central de Aulas II - Sala de aula 04",
    "Central de Aulas II - Sala de aula 05",
    "Central de Aulas II - Sala de aula 06",
    "Central de Aulas II - Sala de aula 07",
    "Central de Aulas II - Sala de aula 08",
    "Central de Aulas II - Sala de aula 11",
    "Central de Aulas II - Sala de aula 12",
    "Central de Aulas II - Sala de aula 14",
    "Central de Aulas II - Sala de aula 15",
    "Central de Aulas II - Sala de aula 16",
    "Centro de Convivência - Auditório do CC",
    "Centro de Convivência - Sala de Lutas / Atividades Físicas",
    "Ginásio - Ginásio",
    "Laboratório de Ciência e Tecnologia - Laboratório de Eletricidade e Magnetismo",
    "Laboratório de Ciência e Tecnologia - Laboratório de Informática 01",
    "Laboratório de Ciência e Tecnologia - Laboratório de Informática 02",
    "Laboratório de Ciência e Tecnologia - Laboratório de Mecânica Clássica",
    "Laboratório de Ciência e Tecnologia - Laboratório de Ondas e Termodinâmica",
    "Laboratório de Ciência e Tecnologia - Laboratório de Química Aplicada a Engenharia",
    "Laboratório de Ciência e Tecnologia - Laboratório de Química Geral",
    "Laboratório de Ciência e Tecnologia - Sala de aula 01",
    "Laboratório de Tecnologia da Informação - Auditório",
    "Laboratório de Tecnologia da Informação - Laboratório de Automação",
    "Laboratório de Tecnologia da Informação - Laboratório de Eletrônica",
    "Laboratório de Tecnologia da Informação - Laboratório de Informática 01",
    "Laboratório de Tecnologia da Informação - Laboratório de Informática 02",
    "Laboratório de Tecnologia da Informação - Sala de aula 01",
    "Laboratório de Tecnologia da Informação - Sala de aula 02",
    "Laboratório de Tecnologia da Informação - Sala de aula 03",
    "Laboratório de Tecnologia da Informação - Sala de aula 04",
    "Laboratórios das Engenharias - Laboratório Arquitetônico I",
    "Laboratórios das Engenharias - Laboratório Arquitetônico II",
    "Laboratórios das Engenharias - Laboratório Arquitetônico III",
    "Laboratórios das Engenharias - Laboratório de Conforto Ambiental",
    "Laboratórios das Engenharias - Laboratório de Geologia, Pavimentação e Solos",
    "Laboratórios das Engenharias - Laboratório de Instalações Hidrossanitárias",
    "Laboratórios das Engenharias - Laboratório de Materiais de Construção",
    "Laboratórios das Engenharias - Laboratório de Microbiologia",
    "Laboratórios das Engenharias - Laboratório de Poluição Ambiental",
    "Laboratórios das Engenharias - Laboratório de Química Ambiental",
    "Laboratórios das Engenharias - Laboratório de Saneamento e Hidráulica",
    "Professores I - Auditório dos professores",
    "Professores I - Sala Multiuso das Coordenações de Curso",
    "Professores II - Ateliê Multiuso de Arquitetura",
]


def resetar_localizacoes(apps, schema_editor):
    Localizacao = apps.get_model("patrimonios", "Localizacao")

    # Apagar tudo
    Localizacao.objects.all().delete()

    # Criar localizações padrões
    for nome in LOCALIZACOES_PADRAO:
        Localizacao.objects.create(nome=nome)


class Migration(migrations.Migration):

    dependencies = [
        ('patrimonios', '0002_localizacao_alter_patrimonio_localizacao'),
    ]

    operations = [
        migrations.RunPython(resetar_localizacoes, migrations.RunPython.noop),
    ]
