from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index', views.index, name = 'index'),
    path('proceso', views.proceso, name = 'proceso'),
    path('tarjeta', views.tarjeta, name = 'tarjeta'),
]