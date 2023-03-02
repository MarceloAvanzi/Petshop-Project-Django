from django.db import models
from django.contrib.auth.models import User

class DadosPagamentos(models.Model):
    # NomeNoCartao = models.CharField(max_length=256,blank=False)
    # NumeroNoCartao = models.CharField(max_length=256,blank=False)
    # ValidadeCartao = models.DateField(blank=False)
    # cvv = models.IntegerField(blank=False)
    Plano = models.CharField(max_length=256,blank=False)
    Banhos = models.IntegerField(blank=False)
    Tosas = models.IntegerField(blank=False)
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.Plano
