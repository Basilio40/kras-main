from django.contrib import admin
from ordem_de_servico import models
# Register your models here.
class OrdemAdmin(admin.ModelAdmin):
    model = models.Ordem
    list_display = ('cliente','modalidade', 'executante', 'responsavel', 'entrega_prevista', 'abertura_OS')

admin.site.register(models.Ordem, OrdemAdmin)