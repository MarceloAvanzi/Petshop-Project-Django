from importlib.resources import path
from .views import HomeView
from django.urls import path

urlpatterns = [
    path('',    HomeView.as_view(), name='home') # deixa path vazio pq é o index do site, url vazia direciona pro home
]
