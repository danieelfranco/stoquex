from django import forms
from .models import Equipamento


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ["nome", "numero_serie", "status", "data_aquisicao", "responsavel"]