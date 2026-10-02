from django.contrib import admin
from .models import Funcionario, Equipamento

# Register your models here.

class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ("nome",  "numero_serie", "status", "responsavel")

admin.site.register(Funcionario)
admin.site.register(Equipamento, EquipamentoAdmin)