import email
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

class PetsUsuario(models.Model):
    nome_completo = models.CharField(max_length=256)
    raça = models.CharField(max_length=256)
    porte = models.CharField(max_length=256)
    idade = models.IntegerField()
    ativa = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nome_completo