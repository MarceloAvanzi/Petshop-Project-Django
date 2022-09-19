from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import PetsUsuario
from .forms import PetForm

class ListaPetsUsuarios(ListView):
    model = PetsUsuario
    queryset = PetsUsuario.objects.all().order_by('nome_completo') #dentro da tabela Pessoa, pega tudo oq tem na lista 

    #Aplicar filtros na busca
    def get_queryset(self):
        queryset =  super().get_queryset()
        #queryset = queryset.filter(usuario=self.request.user)
        filtro_nome = self.request.GET.get('filtronome') or None
        if filtro_nome:
            queryset = queryset.filter(nome_completo__contains=filtro_nome)

        return queryset

class CadastrarPet(CreateView):
    model = PetsUsuario
    form_class = PetForm
    success_url = '/usuario/'

class EditarPet(UpdateView):
    model = PetsUsuario
    form_class = PetForm
    success_url = '/usuario/'

class DeletarPet(DeleteView):
    model = PetsUsuario
    success_url = '/usuario/'