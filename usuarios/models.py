from django.db import models
from datetime import date
from Alunos.models import AlunosIspk

class Usuarios(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Livros(models.Model):
    nome = models.CharField(max_length = 255)
    autor = models.CharField(max_length = 100)
    data_cadastro = models.DateField(default = date.today)
    emprestado = models.BooleanField(default = False)
    nome_emprestado = models.CharField(max_length = 100)
    data_emprestimo = models.DateTimeField(blank = True, null= True)
    data_devolucao = models.DateTimeField(blank = True, null = True)
    tempo_duracao = models.DateField(blank = True, null= True)

    class Meta:
        verbose_name = 'Livros da Biblioteca'

    def __str__(self):
        return self.nome



