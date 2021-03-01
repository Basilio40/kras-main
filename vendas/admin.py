from django.contrib import admin
from vendas import models

# Register your models here.

class VendasAdmin(admin.ModelAdmin):
    model = models.Vendas
    list_display = ()

admin.site.register(models.Vendas, VendasAdmin)


