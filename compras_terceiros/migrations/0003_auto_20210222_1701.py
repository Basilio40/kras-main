# Generated by Django 3.1.7 on 2021-02-22 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras_terceiros', '0002_auto_20210222_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='an',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='descricao',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='desloc_km',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='he',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='he_percent',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='ht',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='notafiscal',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='pedagio',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='qtd',
        ),
        migrations.RemoveField(
            model_name='comprasteceiros',
            name='tipo',
        ),
    ]
