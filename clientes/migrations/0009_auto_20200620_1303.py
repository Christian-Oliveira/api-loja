# Generated by Django 2.2.13 on 2020-06-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0008_auto_20200616_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('F', 'FEMININO'), ('M', 'MASCULINO')], max_length=1),
        ),
    ]