from multiprocessing import context
from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import login
from django.views.generic import UpdateView
from .models import UserLogin

from mainpage.forms import NovoUsuarioForm

# Create your views here.
class HomeView(TemplateView):
    template_name = 'main/index.html'

class SobreNosView(TemplateView):
    template_name = 'main/sobrenos.html'


def Registrar(request):
    if request.method == "POST":
        form = NovoUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect('home')
        messages.error(request, "Falha no cadastro do usuário.")
    form = NovoUsuarioForm()
    context = {'form': form}
    return render(request, template_name='registration/registrar.html', context=context)

class EditarCadastro(UpdateView):
    model = UserLogin
    form_class = NovoUsuarioForm
    success_url = '/usuario/'