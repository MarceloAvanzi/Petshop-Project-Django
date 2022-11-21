from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView, TemplateView
from .models import Usuario
from .forms import PetForm,FormAgendamento

class ListaPets(ListView):
    model = Usuario
    queryset = Usuario.objects.all().order_by('nome') #dentro da tabela Pessoa, pega tudo oq tem na lista 
    #Aplicar filtros na busca
    def get_queryset(self):
        queryset =  super().get_queryset()
        queryset = queryset.filter(usuariologado=self.request.user)
        filtro_nome = self.request.GET.get('filtronome') or None
        if filtro_nome:
            queryset = queryset.filter(nome__contains=filtro_nome)
        return queryset


class CadastrarPet(CreateView): #CadastrarPet
    model = Usuario
    form_class = PetForm
    success_url = '/usuario/'
    def form_valid(self, form):
        form.instance.usuariologado = self.request.user
        return super().form_valid(form)


class EditarPet(UpdateView): #EditarPet
    model = Usuario
    form_class = PetForm
    success_url = '/usuario/'


class DeletarPet(DeleteView): #DeletarPet
    model = Usuario
    success_url = '/usuario/'



# Pagina de Agendar horario

def AgendamentoView(request):
    form = FormAgendamento()
    model = Usuario.objects.all().order_by('nome')
    return render(request,'agendar/agendarhorario.html',{'form': form,'pets': model})















# def MeusPets(request, pk_usuario):
#     MeusPets = Pets.objects.filter(pessoa=pk_usuario)
#     return render(request, 'pets/pet_list.html', {'MeusPets': MeusPets, 'pk_usuario':pk_usuario})

# def CadastrarPet(request, pk_usuario):
#     form = MeuPetForm()
#     if request.method == "POST":
#         form = MeuPetForm(request.POST)
#         if form.is_valid():
#             contato = form.save(commit=False)
#             contato.pessoa_id = pk_usuario
#             contato.save()
#             return redirect(reverse('usuario.meuspets', args=[pk_usuario]))

#     return render(request, 'pets/pet_form.html', {'form': form})


# def EditarPet(request, pk_usuario, pk):
#     contato = get_object_or_404(Pets, pk=pk)
#     form = MeuPetForm(instance=contato)
#     if request.method == "POST":
#         form = MeuPetForm(request.POST, instance=contato)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('usuario.meuspets', args=[pk_usuario]))

#     return render(request, 'pets/pet_form.html', {'form': form})


# def DeletarPet(request, pk_usuario, pk):
#     contato = get_object_or_404(Pets, pk=pk)
#     contato.delete()
#     return redirect(reverse('usuario.meuspets', args=[pk_usuario]))