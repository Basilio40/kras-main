# Generated by Django 3.1.6 on 2021-02-15 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_auto_20210215_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modalidade',
            name='descricao',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='servico',
            name='descricao',
            field=models.CharField(max_length=100),
        ),
    ]