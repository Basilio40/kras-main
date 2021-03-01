from django.contrib import admin
from compras import models

# Register your models here.

class ComprasAdmin(admin.ModelAdmin):
    model = models.Compras
    list_display = ()

admin.site.register(models.Compras, ComprasAdmin)


