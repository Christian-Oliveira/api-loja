# Generated by Django 2.2.13 on 2020-06-16 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0006_auto_20200615_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(error_messages={'unique': 'Um Cliente com este CPF já existe.'}, max_length=11, unique=True),
        ),
    ]
