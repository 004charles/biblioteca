from django.contrib import admin
from django.urls import path, include
from usuarios import views  


urlpatterns = [
    path('login/', views.login, name='login'),
    path('index/', views.index, name='index'),
    path('inicio/', views.inicio, name='inicio'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('emprestimo/', views.emprestimo, name = 'emprestimo'),
    path('devolucao/', views.devolucao, name = 'devolucao'),
    path('user/', views.user, name = 'user'),
    path('livros-mais-emprestados/', views.livros_mais_emprestados, name='livros-mais-emprestados'),
    path('livros/', views.livros, name = 'livros'),
    path('valida_cadastro_cliente/', views.valida_cadastro_cliente, name='valida_cadastro_cliente'),
    path('valida_login_cliente/', views.valida_login_cliente, name='valida_login_cliente'),
]

