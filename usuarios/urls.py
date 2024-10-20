from django.contrib import admin
from django.urls import path, include
from usuarios import views  


urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('inicio/', views.inicio, name='inicio'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('valida_cadastro_cliente/', views.valida_cadastro_cliente, name='valida_cadastro_cliente'),
    path('valida_login_cliente/', views.valida_login_cliente, name='valida_login_cliente'),
]

