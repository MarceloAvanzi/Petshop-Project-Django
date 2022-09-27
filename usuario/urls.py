from django import views
from django.urls import path
from .views import EditarUsuario, ListaUsuarios,CadastrarUsuario,DeletarUsuario
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',login_required(ListaUsuarios.as_view()),name='usuario.home'),
    path('cadastrarusuario/',login_required(CadastrarUsuario.as_view()),name='usuario.cadastrarusuario'),
    path('<int:pk>/editarusuario',login_required(EditarUsuario.as_view()),name='usuario.editarusuario'),
    path('<int:pk>/deletarusuario',login_required(DeletarUsuario.as_view()),name='usuario.deletarusuario'),
    path('<int:pk_usuario>/meuspets',login_required(views.MeusPets),name='usuario.meuspets'),
    path('<int:pk_usuario>/cadastrarpet',login_required(views.CadastrarPet),name='pets.cadastrarpet'),
    path('<int:pk_usuario>/editarpet/<int:pk>/editar',login_required(views.EditarPet),name='pets.editarpet'),
    path('<int:pk_usuario>/deletarpet/<int:pk>/deletar',login_required(views.DeletarPet),name='pets.deletarpet'),
]
