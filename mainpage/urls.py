from importlib.resources import path
from .views import HomeView, Registrar, SobreNosView,EditarCadastro
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', HomeView.as_view(), name='home'), # deixa path vazio pq é o index do site, url vazia direciona pro home
    path('sobrenos', SobreNosView.as_view(), name='sobrenos'), # O name é oq eu listo no href do html e o começo é oq aparece na url da pagina
    path('accounts/registrar', Registrar, name='registrar')
]
