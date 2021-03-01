from django.contrib import admin
from proposta import models

# Register your models here.

class PropostaAdmin(admin.ModelAdmin):
    model = models.Proposta
    list_display = ()

admin.site.register(models.Proposta, PropostaAdmin)