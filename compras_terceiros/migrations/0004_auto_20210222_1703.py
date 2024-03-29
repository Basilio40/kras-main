# Generated by Django 3.1.7 on 2021-02-22 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras_terceiros', '0003_auto_20210222_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprasteceiros',
            name='an',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comprasteceiros',
            name='he',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comprasteceiros',
            name='he_percent',
            field=models.CharField(blank=True, choices=[('50', '50%'), ('75', '75%'), ('100', '100%')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='comprasteceiros',
            name='ht',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='comprasteceiros',
            name='notafiscal',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='comprasteceiros',
            name='qtd',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
