# Generated by Django 3.1.7 on 2021-02-28 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0016_compras'),
        ('compras', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='compras',
            name='Data',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='compras',
            name='PG',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='compras',
            name='PG_IT',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='compras',
            name='cod_fornec',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cadastro.fornecedor'),
        ),
        migrations.AddField(
            model_name='compras',
            name='detalhamento',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='compras',
            name='notafiscal',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='compras',
            name='pagamento',
            field=models.CharField(blank=True, choices=[('pago', 'Pago'), ('naopago', 'Não Pago')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='compras',
            name='quantidade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='compras',
            name='status_ps',
            field=models.CharField(blank=True, choices=[('enviado', 'Enviado'), ('emitido', 'Emitido'), ('naoemitido', 'Não Emitido')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='compras',
            name='unidade',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
