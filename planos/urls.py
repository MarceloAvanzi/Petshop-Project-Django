from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import Home,pagarme_page


urlpatterns=[
    path('',login_required(Home),name='planos.home'),
    path('pagarme/',login_required(pagarme_page),name='planos.pagarmepage'),
]