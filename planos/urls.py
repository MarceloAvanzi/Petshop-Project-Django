from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import AssinaturasView


urlpatterns=[
    path('',login_required(AssinaturasView),name='planos.home'),
]