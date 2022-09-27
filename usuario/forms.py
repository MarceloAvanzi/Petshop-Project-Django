from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Usuario, Pets

class UsuarioForm(ModelForm): #PetForm
    #celular = forms.
    class Meta:
        model = Usuario
        fields = ['nome_completo','email','celular','idade','ativa']

class MeuPetForm(ModelForm):
    class Meta:
        model = Pets
        fields =['nome','raça','porte','idade','ativa']