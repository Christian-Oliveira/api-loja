# Generated by Django 2.2.13 on 2020-06-15 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_auto_20200614_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='ponto_ref',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
