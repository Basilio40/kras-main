from django.db import models
from cadastro import models as cadastro_models


# Create your models here.
class Compras(models.Model):
    PC_CHOICES = (
        ('enviado', "Enviado"),
        ('emitido', "Emitido"),
        ('naoemitido', "Não Emitido")
    )
    PAGAMENTO_CHOICE = (
        ('pago', "Pago"),
        ('naopago', "Não Pago")
    )
    PG = models.CharField(max_length=100, null=True, blank=True)
    PG_IT = models.CharField(max_length=100, null=True, blank=True)
    Data = models.DateField(null=True, blank=True)
    descricao = models.ManyToManyField(cadastro_models.Compras,null=True, blank=True)
    unidade = models.CharField(max_length=50, null=True,  blank=True)
    quantidade = models.IntegerField(null=True, blank=True)
    cod_fornec = models.ForeignKey(cadastro_models.Fornecedor,on_delete=models.CASCADE,null=True, blank=True)
    status_ps = models.CharField(max_length=100, choices=PC_CHOICES,null=True, blank=True)
    pagamento = models.CharField(max_length=100, choices=PAGAMENTO_CHOICE, null=True, blank=True)
    notafiscal = models.CharField(max_length=150, null=True, blank=True)
    # OS = precisamos definir
    # OS_IT = precisamos definir
    detalhamento =  models.CharField(max_length=200, null=True, blank=True)
    # centrocusto = models.ForeignKey(cadastro_models.Compras.centrocusto,on_delete=models.CASCADE,null=True, blank=True)
    # fornecedor = models.ForeignKey(cadastro_models.Fornecedor, on_delete=models.SET_NULL, null=True, blank=True, related_name="nome")
    custo_pedido = models.DecimalField(max_digits=50,decimal_places=10, null=True, blank=True)
    # cliente = models.ForeignKey(cadastro_models.Cliente, on_delete=models.CASCADE)
    


    class Meta:
        verbose_name = "Compra "
        verbose_name_plural = "Compras "



