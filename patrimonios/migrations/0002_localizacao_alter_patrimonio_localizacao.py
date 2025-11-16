from django.db import migrations, models

def migrar_localizacoes(apps, schema_editor):
    Patrimonio = apps.get_model("patrimonios", "Patrimonio")
    Localizacao = apps.get_model("patrimonios", "Localizacao")

    nomes_existentes = (
        Patrimonio.objects
        .values_list("localizacao", flat=True)
        .distinct()
    )

    mapa = {}

    for nome in nomes_existentes:
        if nome and nome.strip():
            loc = Localizacao.objects.create(nome=nome.strip())
            mapa[nome] = loc.id

    for p in Patrimonio.objects.all():
        if p.localizacao in mapa:
            p.localizacao_fk_id = mapa[p.localizacao]
            p.save(update_fields=["localizacao_fk_id"])


class Migration(migrations.Migration):

    dependencies = [
        ('patrimonios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Localizacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150, unique=True)),
            ],
        ),

        migrations.AddField(
            model_name='patrimonio',
            name='localizacao_fk',
            field=models.ForeignKey(
                to='patrimonios.Localizacao',
                null=True,
                blank=True,
                on_delete=models.SET_NULL
            ),
        ),

        migrations.RunPython(migrar_localizacoes, migrations.RunPython.noop),

        migrations.RemoveField(
            model_name='patrimonio',
            name='localizacao',
        ),

        migrations.RenameField(
            model_name='patrimonio',
            old_name='localizacao_fk',
            new_name='localizacao',
        ),
    ]
