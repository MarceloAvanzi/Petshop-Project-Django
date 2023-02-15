from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# class CadastroUsuario(models.Model):
#     nome_completo = models.CharField(max_length=256, null=True) #campo tipo texto livre pra pessoa preencher
#     email = models.EmailField(max_length=256, null=True)
#     data_nascimento = models.DateField(null=True)
#     cpf = models.CharField(max_length=14, null=True)
#     celular = models.CharField(max_length=16, null=True)
#     usuario = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return self.nome_completo

class Usuario(models.Model): #PetsUsuario
    nome = models.CharField(max_length=256)
    raça = models.CharField(max_length=256)
    porte = models.CharField(max_length=256)
    idade = models.IntegerField()
    ativa = models.BooleanField(default=True)
    usuariologado = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome

# variaveis que terão na pagina de agendamento
class Agendamento(models.Model):
    data = models.DateField()
    horario = models.CharField(max_length=5)
    banho = models.BooleanField(default=False, blank=False)
    TOSAS = (
        ('Completa', ('Tosa Completa')),
        ('Higienica', ('Tosa Higiênica')),
        ('Não', ('Sem Tosa')),
    )
    tosa = models.CharField(choices=TOSAS ,max_length=256)
    pulgas = models.BooleanField(default=False)
    observacao = models.CharField(max_length=256)
    usuariologado = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.horario






# class Pets(models.Model): #Contato
#     nome = models.CharField(max_length=256)
#     raça = models.CharField(max_length=256)
#     porte = models.CharField(max_length=256)
#     idade = models.IntegerField()
#     ativa = models.BooleanField(default=True)
#     pessoa = models.ForeignKey(Usuario, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return self.nome