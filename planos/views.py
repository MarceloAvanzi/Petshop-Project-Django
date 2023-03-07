from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from .models import DadosPagamentos


def AssinaturasView(request):
    dadosPagamentos = DadosPagamentos.objects.all().order_by('Plano')
    return render(request,'planos.html',{'dadosPag': dadosPagamentos})

# class Assinaturas(ListView):
#     model = DadosPagamentos
#     template_name = "planos.html"

#     def GetVariableFromStatic(request):
#         myvar = request.GET['data']
#         print(myvar)
#         breakpoint()
#         return myvar

