from pyclbr import Function
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'main/index.html'

class SobreNosView(TemplateView):
    template_name = 'main/sobrenos.html'
