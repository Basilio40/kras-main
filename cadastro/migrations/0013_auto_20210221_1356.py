# Generated by Django 3.1.7 on 2021-02-21 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0012_auto_20210221_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='colaborador',
            name='bairro',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='cep',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='colaborador',
            name='numero',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
