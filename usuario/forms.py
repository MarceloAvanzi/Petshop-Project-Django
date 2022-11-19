from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Usuario,Agendamento

class PetForm(ModelForm): #PetForm
    class Meta:
        model = Usuario
        fields = ['nome','raça','porte','idade','ativa']


class FormAgendamento(ModelForm):
    class Meta:
        model = Agendamento
        fields = ['data','horario','banho','tosa','pulgas','observacao']

# class MeuPetForm(ModelForm):
#     class Meta:
#         model = Pets
#         fields =['nome','raça','porte','idade','ativa']