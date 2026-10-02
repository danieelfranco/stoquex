from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipamento
from .forms import EquipamentoForm


def lista_equipamento(request):
    equipamentos = Equipamento.objects.all()
    return render(request, "equipamentos/lista_equipamentos.html", {"equipamentos": equipamentos})


def detalhe_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    return render(request, "equipamentos/detalhe_equipamento.html", {"equipamento": equipamento})


def cadastrar_equipamento(request):
    if request.method == "POST":
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_equipamentos")
    else:
        form = EquipamentoForm()
    return render(request, "equipamentos/cadastrar_equipamento.html", {"form": form, "titulo": "Cadastrar equipamento"})

def editar_equipamento (request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        form = EquipamentoForm(request.POST, instance=equipamento)
        if form.is_valid():
            form.save()
            return redirect('detalhe_equipamento', pk=pk)
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'equipamentos/cadastrar_equipamento.html', {'form': form, 'titulo': 'Editar equipamento'})

def excluir_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        equipamento.delete()
        return redirect('lista_equipamentos')
    return render(request, 'equipamentos/confirmar_exclusao.html', {'equipamento': equipamento})