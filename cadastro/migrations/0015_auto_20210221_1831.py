# Generated by Django 3.1.7 on 2021-02-21 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0014_auto_20210221_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='dia_pagamento',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='valor_contrato',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=19, null=True),
        ),
    ]
