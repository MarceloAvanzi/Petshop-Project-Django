from django.db import models
from django.contrib.auth.models import User

class DadosPagamentos(models.Model):
    # NomeNoCartao = models.CharField(max_length=256,blank=False)
    # NumeroNoCartao = models.CharField(max_length=256,blank=False)
    # ValidadeCartao = models.DateField(blank=False)
    # cvv = models.IntegerField(blank=False)
    Plans = (
        ('Basic', ('Basic')),
        ('Standard', ('Standard')),
        ('Premium', ('Premium')),
    )
    Planos = models.BooleanField(choices=Plans ,max_length=256, blank=True)
    Banhos = models.IntegerField(default=0)
    Tosas = models.IntegerField(default=0)
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.Plano
