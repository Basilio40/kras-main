from django.db import models
from cadastro import models as cadastro_models


# Create your models here.
class Vendas(models.Model):
    # ATRIBUICAO_CHOICES = (
    #     ('exe', "Executante"),
    #     ('resp', "Responsável")
    # )
    PV = models.CharField(max_length=100, null=True, blank=True)
    PV_IT = models.CharField(max_length=100, null=True, blank=True)
    # OS = precisamos definir
    # OS_IT = precisamos definir
    servicos = models.ManyToManyField(cadastro_models.Servico)
    executante = models.ForeignKey(cadastro_models.Colaborador, on_delete=models.CASCADE)
    data = models.DateField(null=True, blank=True)
    cliente = models.ForeignKey(cadastro_models.Cliente, on_delete=models.CASCADE)
    detalhamento = models.CharField(max_length=200, null=True, blank=True)
    HT = models.FloatField(default=0)
    QTD = models.IntegerField(default=0)
    HE = models.FloatField(default=0)
    HE_percentual = models.FloatField(default=0)
    AN = models.FloatField(default=0)
    preco_servico = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    tipo = models.CharField(max_length=100, null=True, blank=True)
    adicional = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    descricao_venda = models.CharField(max_length=100, null=True, blank=True)
    preco_venda = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    filtro_desloc = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    filtro_serv = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)
    # custo_HH = 
    # despesas = 
    # compras_terceiros = 
    # compras = 
    # impostos = 
    # lucro_liquido = 
    # percentual = 
    # conceito = 


    class Meta:
        verbose_name = "Venda "
        verbose_name_plural = "Vendas "

