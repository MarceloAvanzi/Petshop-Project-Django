from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import Assinaturas


urlpatterns=[
    path('',login_required(Assinaturas.as_view()),name='planos.home'),
]