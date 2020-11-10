# Generated by Django 2.2.13 on 2020-11-10 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_auto_20200831_1600'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venda',
            name='preco_final',
        ),
        migrations.AddField(
            model_name='venda',
            name='status',
            field=models.CharField(choices=[('P', 'PENDENTE'), ('F', 'FINALIZADO')], max_length=1, null=True, verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='venda',
            name='valor_pago',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Valor Pago'),
        ),
        migrations.CreateModel(
            name='Parcelas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_parcelas', models.PositiveSmallIntegerField(verbose_name='Número de Parcelas')),
                ('valor_parcela', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor da Parcela')),
                ('venc_parcela', models.DateField()),
                ('status', models.CharField(choices=[('A', 'ABERTO'), ('V', 'VENCIDO'), ('P', 'PAGO')], default='A', max_length=1, verbose_name='Status')),
                ('data_pagamento', models.DateField(blank=True, null=True)),
                ('juros', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('valor_pago', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('id_venda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parcelas', to='vendas.Venda')),
            ],
        ),
    ]
