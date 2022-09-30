from django.urls import path
from .views import EditarPet, ListaPets,CadastrarPet,DeletarPet
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',login_required(ListaPets.as_view()),name='usuario.home'),
    path('cadastrarusuario/',login_required(CadastrarPet.as_view()),name='pet.cadastrarusuario'),
    path('<int:pk>/editarusuario',login_required(EditarPet.as_view()),name='pet.editarusuario'),
    path('<int:pk>/deletarusuario',login_required(DeletarPet.as_view()),name='pet.deletarusuario'),


    
    # path('<int:pk_usuario>/meuspets',login_required(views.MeusPets),name='usuario.meuspets'),
    # path('<int:pk_usuario>/cadastrarpet',login_required(views.CadastrarPet),name='pets.cadastrarpet'),
    # path('<int:pk_usuario>/editarpet/<int:pk>/editar',login_required(views.EditarPet),name='pets.editarpet'),
    # path('<int:pk_usuario>/deletarpet/<int:pk>/deletar',login_required(views.DeletarPet),name='pets.deletarpet'),
]