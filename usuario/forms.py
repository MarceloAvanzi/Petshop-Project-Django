from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import PetsUsuario

class PetForm(ModelForm):
    class Meta:
        model = PetsUsuario
        fields = ['nome_completo','raça','porte','idade','ativa']