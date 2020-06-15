# Generated by Django 2.2.13 on 2020-06-15 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_usuario', models.PositiveSmallIntegerField(choices=[(1, 'VENDEDOR'), (2, 'CAIXA'), (3, 'SUPERVISOR'), (4, 'ADMINISTRADOR')], default=1)),
                ('sexo', models.PositiveSmallIntegerField(choices=[(1, 'FEMININO'), (2, 'MASCULINO')])),
            ],
        ),
    ]
