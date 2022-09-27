from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import Usuario,Pets
from .forms import UsuarioForm, MeuPetForm

class ListaUsuarios(ListView):
    model = Usuario
    queryset = Usuario.objects.all().order_by('nome_completo') #dentro da tabela Pessoa, pega tudo oq tem na lista 

    #Aplicar filtros na busca
    def get_queryset(self):
        queryset =  super().get_queryset()
        #queryset = queryset.filter(usuario=self.request.user)
        filtro_nome = self.request.GET.get('filtronome') or None
        if filtro_nome:
            queryset = queryset.filter(nome_completo__contains=filtro_nome)

        return queryset

class CadastrarUsuario(CreateView): #CadastrarPet
    model = Usuario
    form_class = UsuarioForm
    success_url = '/usuario/'

class EditarUsuario(UpdateView): #EditarPet
    model = Usuario
    form_class = UsuarioForm
    success_url = '/usuario/'

class DeletarUsuario(DeleteView): #DeletarPet
    model = Usuario
    success_url = '/usuario/'


def MeusPets(request, pk_usuario):
    MeusPets = Pets.objects.filter(pessoa=pk_usuario)
    return render(request, 'pets/pet_list.html', {'MeusPets': MeusPets, 'pk_usuario':pk_usuario})

def CadastrarPet(request, pk_usuario):
    form = MeuPetForm()
    if request.method == "POST":
        form = MeuPetForm(request.POST)
        if form.is_valid():
            contato = form.save(commit=False)
            contato.pessoa_id = pk_usuario
            contato.save()
            return redirect(reverse('usuario.meuspets', args=[pk_usuario]))

    return render(request, 'pets/pet_form.html', {'form': form})


def EditarPet(request, pk_usuario, pk):
    contato = get_object_or_404(Pets, pk=pk)
    form = MeuPetForm(instance=contato)
    if request.method == "POST":
        form = MeuPetForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            return redirect(reverse('usuario.meuspets', args=[pk_usuario]))

    return render(request, 'pets/pet_form.html', {'form': form})


def DeletarPet(request, pk_usuario, pk):
    contato = get_object_or_404(Pets, pk=pk)
    contato.delete()
    return redirect(reverse('usuario.meuspets', args=[pk_usuario]))