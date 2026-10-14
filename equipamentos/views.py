from django.shortcuts import render, get_object_or_404, redirect
from .models import Equipamento, Funcionario
from .forms import EquipamentoForm, FuncionarioForm
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

def lista_equipamento(request):
    todos = Equipamento.objects.all()

    # Cards: sempre sobre o estoque inteiro
    resumo = []
    for valor, rotulo in Equipamento.STATUS_CHOICES:
        resumo.append({
            "rotulo": rotulo,
            "total": todos.filter(status=valor).count(),
            "classe": valor,
        })

    # Busca e filtro: só a tabela
    q = request.GET.get("q", "").strip()
    status = request.GET.get("status", "")

    equipamentos = todos.order_by("nome")
    if q:
        equipamentos = equipamentos.filter(Q(nome__icontains=q) | Q(numero_serie__icontains=q))
    if status:
        equipamentos = equipamentos.filter(status=status)

    paginator = Paginator(equipamentos, 5)
    pagina = paginator.get_page(request.GET.get("page"))

    return render(request, "equipamentos/lista_equipamentos.html", {
        "equipamentos": pagina,
        "total": todos.count(),
        "resumo": resumo,
        "q": q,
        "status": status,
        "status_choices": Equipamento.STATUS_CHOICES,
    })

def detalhe_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    return render(request, "equipamentos/detalhe_equipamento.html", {"equipamento": equipamento})


def cadastrar_equipamento(request):
    if request.method == "POST":
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            equipamento = form.save()
            messages.success(request, f'Equipamento "{equipamento.nome}" cadastrado com sucesso!')
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
            messages.success(request, f'Equipamento "{equipamento.nome}" atualizado com sucesso!')
            return redirect('detalhe_equipamento', pk=pk)
    else:
        form = EquipamentoForm(instance=equipamento)
    return render(request, 'equipamentos/cadastrar_equipamento.html', {'form': form, 'titulo': 'Editar equipamento'})

def excluir_equipamento(request, pk):
    equipamento = get_object_or_404(Equipamento, pk=pk)
    if request.method == 'POST':
        equipamento.delete()
        messages.success(request, f'Equipamento "{equipamento.nome}" excluído.')
        return redirect('lista_equipamentos')
    return render(request, 'equipamentos/confirmar_exclusao.html', {'equipamento': equipamento})

def lista_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    return render(request, "equipamentos/lista_funcionarios.html", {"funcionarios": funcionarios})

def cadastrar_funcionario(request):
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            funcionario = form.save()
            messages.success(request, f'Funcionário "{funcionario.nome}" cadastrado com sucesso!')
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
            messages.success(request, f'Funcionário "{funcionario.nome}" atualizado com sucesso!')
            return redirect("lista_funcionarios")
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, "equipamentos/cadastrar_funcionario.html", {"form": form, "titulo": "Editar funcionário"})

def excluir_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == "POST":
        funcionario.delete()
        messages.success(request, f'Funcionário "{funcionario.nome}" excluído.')
        return redirect("lista_funcionarios")
    return render(request, "equipamentos/confirmar_exclusao_funcionario.html", {"funcionario": funcionario})