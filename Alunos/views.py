from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from .models import AlunosIspk
from django.shortcuts import redirect
from django.contrib import messages  # Para enviar mensagens de erro

def Alunos(request):
    return render(request, 'login_alunos.html')

from django.http import JsonResponse

def valida_cadastro_aluno(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        email = request.POST.get('email')
        nivel = request.POST.get('nivel')
        sala = request.POST.get('sala')
        curso = request.POST.get('curso')

        print(f"Nome: {nome}, Senha: {senha}, Email: {email}")

        if not nome or not email or len(nome.strip()) == 0 or len(email.strip()) == 0:
            return JsonResponse({'status': 'error', 'message': 'Nome ou Email em branco.'})

        if len(senha) < 8:
            return JsonResponse({'status': 'error', 'message': 'Senha menor que 8 caracteres.'})

        aluno_exists = AlunosIspk.objects.filter(email=email).exists()

        if aluno_exists:
            return JsonResponse({'status': 'error', 'message': 'Usuário já cadastrado.'})

        try:
            aluno = AlunosIspk(nome=nome, senha=senha, email=email, nivel=nivel, sala=sala, curso=curso)
            aluno.save()
            return JsonResponse({'status': 'success', 'redirect': '/biblioteca/'})  # Redireciona para a biblioteca
        except Exception as e:
            print(f"Erro ao salvar usuário: {e}")
            return JsonResponse({'status': 'error', 'message': 'Erro ao salvar usuário.'})

    return JsonResponse({'status': 'error', 'message': 'Método não permitido.'})


def valida_login_aluno(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        # Verifique se as credenciais estão corretas
        aluno = AlunosIspk.objects.filter(email=email, senha=senha).first()

        if aluno:
            request.session['cliente'] = aluno.id
            return redirect('/ISPK/Biblioteca/')  # Redireciona diretamente para a página Biblioteca
        else:
            messages.error(request, 'Credenciais inválidas')  # Adiciona uma mensagem de erro
            return redirect('/ISPK/Alunos/?status=1')  # Redireciona de volta para a página de login

    return redirect('/ISPK/erro/')  # Renderiza a página caso não seja um POST


def Biblioteca(request):
    return render(request, 'bibliotecas.html')

def Erro(request, exception):
    return render(request, 'erro.html', status=404)