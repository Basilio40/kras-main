# Generated by Django 3.1.6 on 2021-02-15 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cadastro', '0006_auto_20210215_0550'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atribuicao', models.CharField(choices=[('exe', 'Executante'), ('resp', 'Responsável')], max_length=100)),
                ('aptidao', models.BooleanField()),
                ('ASO', models.BooleanField()),
                ('entrega_prevista', models.DateTimeField()),
                ('abertura_OS', models.DateTimeField()),
                ('finalizacao_OS', models.DateTimeField()),
                ('HT', models.FloatField()),
                ('QTD', models.IntegerField()),
                ('adicional', models.FloatField()),
                ('HE', models.FloatField()),
                ('HE_percentual', models.FloatField()),
                ('AN', models.FloatField()),
                ('deslocamento_quilometragem', models.FloatField()),
                ('pedagio', models.FloatField()),
                ('outros', models.FloatField()),
                ('custo', models.FloatField()),
                ('detalhamento', models.TextField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.cliente')),
                ('executante', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='executante_colaborador', to='cadastro.colaborador')),
                ('modalidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modalidade_ordem', to='cadastro.modalidade')),
                ('modalidade_avulsa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modalidade_ordemavulsa', to='cadastro.modalidade')),
                ('qualificacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cadastro.qualificacao')),
                ('responsavel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='responsavel_colaborador', to='cadastro.colaborador')),
                ('servicos', models.ManyToManyField(to='cadastro.Servico')),
            ],
        ),
    ]
