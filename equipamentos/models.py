from django.db import models
from django.contrib.auth.models import User

class Equipamento(models.Model):
    STATUS_DISPONIVEL = 'disponivel'
    STATUS_EM_USO = 'em_uso'
    STATUS_MANUTENCAO = 'manutencao'
   
    STATUS_CHOICES = [
        (STATUS_DISPONIVEL, 'Disponível'),
        (STATUS_EM_USO, 'Em uso'),
        (STATUS_MANUTENCAO, 'Manutenção'),
    ]
   
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel')
    localizacao = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
   
    def __str__(self):
        return self.nome

class UsoEquipamento(models.Model):
    equipamento = models.ForeignKey('Equipamento', on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data_retirada = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.equipamento.nome} - {self.usuario.username}"
