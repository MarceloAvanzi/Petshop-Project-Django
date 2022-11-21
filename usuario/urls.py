from django.urls import path
from .views import EditarPet, ListaPets,CadastrarPet,DeletarPet,AgendamentoView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',login_required(ListaPets.as_view()),name='usuario.home'),
    path('cadastrarpet/',login_required(CadastrarPet.as_view()),name='pet.cadastrarpet'),
    path('<int:pk>/editarpet',login_required(EditarPet.as_view()),name='pet.editarpet'),
    path('<int:pk>/deletarpet',login_required(DeletarPet.as_view()),name='pet.deletarpet'),
    path('agendarhorario/',login_required(AgendamentoView),name='agendarhorario'),


    
    # path('<int:pk_usuario>/meuspets',login_required(views.MeusPets),name='usuario.meuspets'),
    # path('<int:pk_usuario>/cadastrarpet',login_required(views.CadastrarPet),name='pets.cadastrarpet'),
    # path('<int:pk_usuario>/editarpet/<int:pk>/editar',login_required(views.EditarPet),name='pets.editarpet'),
    # path('<int:pk_usuario>/deletarpet/<int:pk>/deletar',login_required(views.DeletarPet),name='pets.deletarpet'),
]