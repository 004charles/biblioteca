from django.contrib import admin
from django.urls import path, include
from usuarios import views  
from django.conf.urls import handler404
from Alunos.views import Erro  

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', views.login, name="login"), 
    path('edjane/', include('usuarios.urls')), 
    path('ISPK/', include('Alunos.urls')),
    
]

handler404 = Erro