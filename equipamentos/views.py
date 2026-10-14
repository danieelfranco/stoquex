from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipamento, Funcionario
from .forms import EquipamentoForm, FuncionarioForm


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
            equipamento = form.save()
            return redirect("detalhe_equipamento", pk=equipamento.pk)
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

def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, "equipamentos/lista_funcionarios.html", {"funcionarios": funcionarios})

def cadastrar_funcionario(request):
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("lista_funcionarios")
    else:
        form = FuncionarioForm()
    return render(request, "equipamentos/cadastrar_funcionario.html", {"form": form, "titulo": "Cadastrar funcionário"})

def editar_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == "POST":
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect("lista_funcionarios")
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, "equipamentos/cadastrar_funcionario.html", {"form": form, "titulo": "Editar funcionário"})

def excluir_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == "POST":
        funcionario.delete()
        return redirect("lista_funcionarios")
    return render(request, "equipamentos/confirmar_exclusao_funcionario.html", {"funcionario": funcionario})