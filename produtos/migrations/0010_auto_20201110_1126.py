# Generated by Django 2.2.13 on 2020-11-10 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0009_produto_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='codigo',
            field=models.CharField(editable=False, max_length=6, null=True, unique=True, verbose_name='Código'),
        ),
    ]
