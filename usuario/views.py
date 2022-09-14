from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import PetsUsuario
from .forms import PetForm

class ListaPetsUsuarios(ListView):
    model = PetsUsuario
    queryset = PetsUsuario.objects.all().order_by('nome_completo') #dentro da tabela Pessoa, pega tudo oq tem na lista 

class CadastrarPet(CreateView):
    model = PetsUsuario
    form_class = PetForm
    success_url = '/usuario/'