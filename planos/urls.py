from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import test


urlpatterns=[
    path('',login_required(test),name='planos.home'),
]