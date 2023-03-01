from django.shortcuts import render
from django.http import HttpResponse


def Home(request):
    return render(request,'planos.html')

def pagarme_page(request):
    return render(request,'pagarme.html')