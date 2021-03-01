from django.db import models

# Create your models here.
class Servico(models.Model):
    GRUPO_CHOICES = (
        ('E', 'Externo'),
        ('I', 'Interno')
    )
    METODO_COBRANCA_CHOICES = (
        ('diaria', "Diária"),
        ('horas', "Horas"),
        ('quantidade', "Quantidade"),
        ('adicional', "Adicional"),
        ('md -50 / dc +50', "MD -50% / DC +50%")
    )
    ATRIBUICAO_CHOICES = (
        ('exe', "Executante"),
        ('resp', "Responsável")
    )
    centro_de_custo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    prazo = models.IntegerField()
    grupo = models.CharField(max_length=100, choices=GRUPO_CHOICES)
    metodo_de_cobranca = models.CharField(max_length=100, choices=METODO_COBRANCA_CHOICES)
    qualificacao = models.CharField(max_length=100)
    atribuicao = models.CharField(max_length=100, choices=ATRIBUICAO_CHOICES)
    def __str__(self):
        return self.descricao
    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

class Colaborador(models.Model):
    CATEGORIA_CHOICES = (
        ('kras', "Kras"),
        ('terceiro', "Terceiro")
    )
    METODO_COBRANCA_CHOICES = (
        ('diaria', "Diária"),
        ('horas', "Horas")
    )
    FORMA_PAGAMENTO_CHOICES = (
        ('boleto', "Boleto"),
        ('debito_conta', "Débito")
    )   
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100, choices=CATEGORIA_CHOICES)
    metodo_cobranca = models.CharField(max_length=100, choices=METODO_COBRANCA_CHOICES, null=True, blank=True)
    valor_diaria =  models.DecimalField( max_digits=19,decimal_places=10,null=True, blank=True)
    valor_hora = models.DecimalField( max_digits=19,decimal_places=10,null=True, blank=True)
    valor_km = models.DecimalField( max_digits=19,decimal_places=10,null=True, blank=True)
    endereço = models.CharField(max_length=100,null=True, blank=True)
    cep = models.CharField(max_length=50,null=True, blank=True)
    numero = models.CharField(max_length=50, null=True,blank=True)
    bairro = models.CharField(max_length=100, null=True,blank=True)
    agencia = models.CharField(max_length=100, null=True,blank=True)
    conta = models.CharField(max_length=100, null=True,blank=True)
    banco = models.IntegerField(null=True,blank=True)
    cpf = models.CharField(max_length=11, blank=True, null=True)
    cnh = models.CharField(max_length=50, null=True, blank=True)
    validade = models.DateField(null=True, blank=True)
    forma_pagamento = models.CharField(max_length=100, choices=FORMA_PAGAMENTO_CHOICES, null=True, blank=True)
    valor_contrato = models.DecimalField( max_digits=19,decimal_places=10,null=True, blank=True)
    dia_pagamento = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Colaboradores"

class Compras(models.Model):
    centrocusto = models.CharField(max_length=50, null=True, blank=True)
    descricao_compras = models.CharField(max_length=100, null=True, blank=True)
    unidade = models.CharField(max_length=20, null=True, blank=True)

class Qualificacao(models.Model):
    id_item = models.IntegerField()
    descricao = models.CharField(max_length=100)
    def __str__(self):
        return self.descricao
    class Meta:
        verbose_name = "Qualificação"
        verbose_name_plural = "Qualificações"
    
class AtribuicaoDeQualificacao(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    qualificacao = models.ForeignKey(Qualificacao, on_delete=models.CASCADE)
    validade = models.DateField(null=True, blank=True)
    valor = models.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        verbose_name = "Qualificação do Colaborador"
        verbose_name_plural = "Qualificações do Colaborador"

class Modalidade(models.Model):
    METODO_COBRANCA_CHOICES = (
        ('diaria', "Diária"),
        ('horas', "Horas"),
        ('quantidade', "Quantidade"),
        ('adicional', "Adicional"),
        ('md -50 / dc +50', "MD -50% / DC +50%")
    )
    centro_custo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    metodo_de_cobranca = models.CharField(max_length=100, choices=METODO_COBRANCA_CHOICES)
    def __str__(self):
        return self.descricao

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    contato = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    cnpj = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=30, null=True, blank=True)
    rua = models.CharField(max_length=100, null=True, blank=True)
    numero = models.CharField(max_length=20, null=True, blank=True)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    contato = models.CharField(max_length=100, null=True, blank=True)
    telefone = models.CharField(max_length=100, null=True, blank=True)
    cnpj = models.CharField(max_length=100, null=True, blank=True)
    cep = models.CharField(max_length=30, null=True, blank=True)
    rua = models.CharField(max_length=100, null=True, blank=True)
    numero = models.CharField(max_length=20, null=True, blank=True)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=2, null=True, blank=True)
    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Fornecedores"