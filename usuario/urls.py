from django import views
from django.urls import path
from .views import EditarUsuario, ListaUsuarios,CadastrarUsuario,DeletarUsuario
from . import views


urlpatterns = [
    path('',ListaUsuarios.as_view(),name='usuario.home'),
    path('cadastrarusuario/',CadastrarUsuario.as_view(),name='usuario.cadastrarusuario'),
    path('<int:pk>/editarusuario',EditarUsuario.as_view(),name='usuario.editarusuario'),
    path('<int:pk>/deletarusuario',DeletarUsuario.as_view(),name='usuario.deletarusuario'),
    path('<int:pk_usuario>/meuspets',views.MeusPets,name='usuario.meuspets'),
    path('<int:pk_usuario>/cadastrarpet',views.CadastrarPet,name='pets.cadastrarpet'),
    path('<int:pk_usuario>/editarpet/<int:pk>/editar',views.EditarPet,name='pets.editarpet'),
    path('<int:pk_usuario>/deletarpet/<int:pk>/deletar',views.DeletarPet,name='pets.deletarpet'),
]
