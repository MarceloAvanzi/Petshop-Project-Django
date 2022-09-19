from django.urls import path
from .views import EditarPet, ListaPetsUsuarios,CadastrarPet,EditarPet,DeletarPet


urlpatterns = [
    path('',ListaPetsUsuarios.as_view(),name='usuario.home'),
    path('cadastrarpet/',CadastrarPet.as_view(),name='usuario.cadastrarpet'),
    path('editarpet/<int:pk>',EditarPet.as_view(),name='usuario.editarpet'),
    path('deletarpet/<int:pk>',DeletarPet.as_view(),name='usuario.deletarpet'),
]
