from django.contrib import admin
from django.urls import path, include
from Alunos import views  


urlpatterns = [
    path('Alunos/', views.Alunos, name = 'Alunos'),
    path('Biblioteca/', views.Biblioteca, name = 'Biblioteca'),
    path('erro/', views.Erro, name = 'erro'),
    path('valida_cadastro_aluno/', views.valida_cadastro_aluno, name='valida_cadastro_aluno'),
    path('valida_login_aluno/', views.valida_login_aluno, name='valida_login_aluno'),

]

