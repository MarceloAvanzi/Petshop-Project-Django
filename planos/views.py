from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpResponse
from .models import DadosPagamentos

# Passar pra class e tentar usar o kwargs la https://stackoverflow.com/questions/56207840/control-requests-to-view-and-template-output-in-django
# def AssinaturasView(request):
#     dadosPagamentos = DadosPagamentos.objects.all().order_by('Plano')
#     data = HttpResponse
#     print(data)
#     return render(request,'planos.html',{'dadosPag': dadosPagamentos})

class Assinaturas(ListView):
    model = DadosPagamentos
    template_name = "planos.html"

    def GetVariableFromStatic(request):
        myvar = request.GET['checkout']
        print(myvar)
        return myvar

