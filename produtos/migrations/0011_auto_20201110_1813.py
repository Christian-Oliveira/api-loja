# Generated by Django 2.2.13 on 2020-11-10 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0010_auto_20201110_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='codigo',
            field=models.CharField(editable=False, max_length=8, null=True, unique=True, verbose_name='Código'),
        ),
    ]
