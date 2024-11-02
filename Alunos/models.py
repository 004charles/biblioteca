from django.db import models

class AlunosIspk(models.Model):
    nome = models.CharField(max_length = 255)
    sala = models.IntegerField()
    curso = models.CharField(max_length=100)
    nivel = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Alunos'

    def __str__(self):
        return self.nome


