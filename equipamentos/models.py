from django.db import models

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    setor = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Equipamento(models.Model) :
    nome = models.CharField(max_length=100)
    numero_serie = models.CharField(max_length=100,unique=True)
    status = models.CharField(max_length=30)
    data_aquisicao = models.DateField(null=True, blank=True)
    responsavel = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


