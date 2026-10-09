from django import forms
from .models import Equipamento


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ["nome", "numero_serie", "status", "data_aquisicao", "responsavel"]
        labels = {
            "nome": "Nome",
            "numero_serie": "Número de série",
            "status": "Status",
            "data_aquisicao": "Data de aquisição",
            "responsavel": "Responsável",
        }
        widgets = {
            "data_aquisicao": forms.DateInput(attrs={"type": "date"}, format="%Y-%m-%d"),
        }