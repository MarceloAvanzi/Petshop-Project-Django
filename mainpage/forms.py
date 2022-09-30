from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserLogin
from django.forms import CharField, fields, models, ModelForm, DateField, TextInput


class NovoUsuarioForm(UserCreationForm):
    data_nascimento = DateField(
        widget=TextInput(
            attrs = {"type": "date"}
        )
    )

    class Meta:
        model = UserLogin
        fields = ("nome", "apelido", "emailfield", "celular", "cpf", "data_nascimento", "password1", "password2")

    def save(self, commit=True):
        user = super(NovoUsuarioForm, self).save(commit=True)
        user.username = user.emailfield
        user.email = user.emailfield
        user.first_name = user.nome
        user.last_name = user.apelido
        if commit:
            user.save()
        return user