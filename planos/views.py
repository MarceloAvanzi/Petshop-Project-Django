from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from .models import DadosPagamentos
from .forms import DadosPagamentosForm


def AssinaturasView(request):
    dadosPagamentos = DadosPagamentos.objects.all().order_by('Planos')
    form = DadosPagamentosForm(request.POST or None)

    return render(request,'planos.html',{'dadosPag': dadosPagamentos, 'form': form})

# class Assinaturas(ListView):
#     model = DadosPagamentos
#     template_name = "planos.html"

#     def GetVariableFromStatic(request):
#         myvar = request.GET['data']
#         print(myvar)
#         breakpoint()
#         return myvar

