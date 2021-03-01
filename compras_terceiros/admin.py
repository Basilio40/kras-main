from django.contrib import admin
from compras_terceiros import models

# Register your models here.

class ComprasTerceirosAdmin(admin.ModelAdmin):
    model = models.ComprasTeceiros
    list_display = ()

admin.site.register(models.ComprasTeceiros, ComprasTerceirosAdmin)

