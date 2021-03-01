from django.contrib import admin
from cadastro import models
# Register your models here.
class ServicoAdmin(admin.ModelAdmin):
    model = models.Servico
    list_display = ('grupo', 'descricao',)
    search_fields = ('descricao',)

class AtribuicaoDeQualificacaoAdmin(admin.TabularInline):
    model = models.AtribuicaoDeQualificacao

class ColaboradorAdmin(admin.ModelAdmin):
    model = models.Colaborador
    list_display = ('nome', 'categoria','valor_diaria','valor_hora','valor_km','endereço',
    'cep','numero','bairro','agencia', 'conta','banco','cpf','cnh','validade','forma_pagamento','valor_contrato','dia_pagamento')
    search_fields = ('nome',)
    inlines = [AtribuicaoDeQualificacaoAdmin]

class ComprasAdmin(admin.ModelAdmin):
    model = models.Compras
    list_display = ('centrocusto', 'descricao_compras','unidade',)
    search_fields = ('centrocusto',)

class QualificacaoAdmin(admin.ModelAdmin):
    model = models.Qualificacao
    list_display = ('id_item', 'descricao',)
    search_fields = ('descricao',)

class ModalidadeAdmin(admin.ModelAdmin):
    model = models.Modalidade
    list_display = ('centro_custo', 'descricao','metodo_de_cobranca',)
    search_fields = ('descricao',)

class ClienteAdmin(admin.ModelAdmin):
    model = models.Cliente
    list_display = ('nome','email','contato', 'telefone','cnpj')
    search_fields = ('nome',)

class FornecedorAdmin(admin.ModelAdmin):
    model = models.Fornecedor
    list_display = ('nome',)
    search_fields = ('nome',)

admin.site.register(models.Servico, ServicoAdmin)
admin.site.register(models.Colaborador, ColaboradorAdmin)
admin.site.register(models.Compras, ComprasAdmin)
admin.site.register(models.Qualificacao, QualificacaoAdmin)
admin.site.register(models.Modalidade, ModalidadeAdmin)
admin.site.register(models.Cliente, ClienteAdmin)
admin.site.register(models.Fornecedor, FornecedorAdmin)