from django.db import models
from cadastro import models as cadastro_models


# Create your models here.
class ComprasTeceiros(models.Model):
    PC_CHOICES = (
        ('env', "Enviado"),
        ('emit', "Emitido"),
        ('nemit', "Não Emitido"),
    )
    PAGAMENTO_CHOICES = (
        ('pg', "Pago"),
        ('npg', "Não Pago"),
    )
    HEPERCENT_CHOICES = (
        ('50', "50%"),
        ('75', "75%"),
        ('100', "100%"),
    )
    DESPESA_CHOICES = (
        ('despesa',"Despesa"),
        ('servico', "Serviço"),
    )
    
    pedidocompra = models.CharField(max_length=100, choices=PC_CHOICES, null=True, blank=True)
    pagamentocompra = models.CharField(max_length=100, choices=PAGAMENTO_CHOICES,null=True, blank=True)
    pcnumero = models.CharField(max_length=100, null=True ,blank=True)
    pcitem = models.CharField(max_length=100, null=True, blank=True)
    notafiscal = models.CharField(max_length=200, null=True, blank=True)
    ht = models.FloatField(null=True, blank=True)
    qtd = models.FloatField(null=True, blank=True)
    he = models.FloatField(null=True, blank=True)
    he_percent= models.CharField(max_length=100, choices=HEPERCENT_CHOICES, null=True, blank=True)
    an = models.FloatField(null=True, blank=True)
    desloc_km = models.FloatField(null=True, blank=True)
    pedagio = models.DecimalField( max_digits=19,decimal_places=10,null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    tipo = models.CharField(max_length=150, choices=DESPESA_CHOICES, null=True, blank=True )
    custo = models.FloatField(null=True, blank=True)
    # cliente = models.ForeignKey(cadastro_models.Cliente, on_delete=models.CASCADE)
    servicos = models.ManyToManyField(cadastro_models.Servico)
    # modalidade = models.ForeignKey(cadastro_models.Modalidade, on_delete=models.SET_NULL, null=True, blank=True, related_name="modalidade_ordem")
    # modalidade_avulsa = models.ForeignKey(cadastro_models.Modalidade, on_delete=models.SET_NULL, null=True, blank=True, related_name="modalidade_ordemavulsa")
    # executante = models.ForeignKey(cadastro_models.Colaborador, on_delete=models.PROTECT, null=True, blank=True, related_name="executante_colaborador")
    # responsavel = models.ForeignKey(cadastro_models.Colaborador, on_delete=models.PROTECT, null=True, blank=True, related_name="responsavel_colaborador")
    
    # qualificacao = models.ForeignKey(cadastro_models.Qualificacao, on_delete=models.SET_NULL, null=True, blank=True)
    # aptidao = models.BooleanField()
    # ASO = models.BooleanField()
    # entrega_prevista = models.DateTimeField()
    # abertura_OS = models.DateTimeField()
    # finalizacao_OS = models.DateTimeField(null=True, blank=True)
    # HT = models.FloatField(default=0)
    # QTD = models.IntegerField(default=0)
    # adicional = models.FloatField(default=0)
    # HE = models.FloatField(default=0)
    # HE_percentual = models.FloatField(default=0)
    # AN = models.FloatField(default=0)
    # deslocamento_quilometragem = models.FloatField(default=0)
    # pedagio = models.FloatField(default=0)
    # outros = models.FloatField(default=0)
    # custo = models.FloatField(default=0)
    # detalhamento = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Compra de Terceirizada"
        verbose_name_plural = "Compras de Terceiros"

