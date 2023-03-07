import datetime
from django.forms import DateField, ModelForm, TextInput, TimeField, TimeInput
from .models import DadosPagamentos

class DadosPagamentosForm(ModelForm):
    class Meta:
        model = DadosPagamentos
        fields = ['Planos','Banhos','Tosas','User']