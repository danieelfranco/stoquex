from django.urls import path
from . import views

urlpatterns = [
    path('listaequipamento/', views.lista_equipamento, name='lista_equipamentos'),
    path('equipamento/<int:pk>/', views.detalhe_equipamento, name='detalhe_equipamento'),
    path('equipamento/novo/', views.cadastrar_equipamento, name='cadastrar_equipamento'),
    path('equipamento/<int:pk>/editar/', views.editar_equipamento, name='editar_equipamento'),
    path('equipamento/<int:pk>/excluir/', views.excluir_equipamento, name='excluir_equipamento'),
    path('funcionarios/', views.lista_funcionarios, name='lista_funcionarios'),
    path('funcionarios/novo/', views.cadastrar_funcionario, name='cadastrar_funcionario'),
    path('funcionarios/<int:pk>/editar/', views.editar_funcionario, name='editar_funcionario'),
    path('funcionarios/<int:pk>/excluir/', views.excluir_funcionario, name='excluir_funcionario'),
]

