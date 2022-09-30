from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserLogin(User):
    nome = models.CharField(max_length=256,verbose_name="Nome")
    apelido = models.CharField(max_length=256,verbose_name="Apelido",null=True)
    emailfield = models.EmailField(verbose_name="E-mail")
    celular = models.CharField(max_length=256,verbose_name="Celular")
    cpf = models.CharField(max_length=14,verbose_name="CPF")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento",null=True)

USERNAME_FIELD = 'emailfield'
REQUIRED_FIELDS = ['*']