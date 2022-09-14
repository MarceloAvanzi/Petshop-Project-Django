from django.urls import path
from .views import ListaPetsUsuarios,CadastrarPet


urlpatterns = [
    path('',ListaPetsUsuarios.as_view(),name='usuario.home'),
    path('cadastrarpet/',CadastrarPet.as_view(),name='usuario.cadastrarpet')
]
