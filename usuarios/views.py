from django.shortcuts import render, redirect
from .models import Usuarios, Livros
from django.db.models import Count


def index(request):
    return render(request, 'index.html')

def login(request):
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})

def cadastro(request):
    status = request.GET.get('status')
    return render(request, 'cadastro_cliente.html', {'status': status})

def valida_cadastro_cliente(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        email = request.POST.get('email')

        print(f"Nome: {nome}, Senha: {senha}, Email: {email}")

        if not nome or not email or len(nome.strip()) == 0 or len(email.strip()) == 0:
            print("Erro: Nome ou Email em branco.")
            return redirect('/edjane/cadastro/?status=9')

        if len(senha) < 8:
            print("Erro: Senha menor que 8 caracteres.")
            return redirect('/edjane/cadastro/?status=10')

        usuarios_existente = Usuarios.objects.filter(email=email).exists()

        if usuarios_existente:
            print("Erro: Usuário já cadastrado.")
            return redirect('/edjane/cadastro/?status=11')

        try:
            usuario = Usuarios(nome=nome, senha=senha, email=email)
            usuario.save()
            print("Usuário salvo com sucesso.")
            return redirect('/edjane/cadastro/?status=1')
        except Exception as e:
            print(f"Erro ao salvar usuário: {e}")
            return redirect('/vetor5/cadastro_cliente/?status=4')

    return redirect('/edjane/cadastro/')  # Caso o método não seja POST, redireciona para o cadastro

def valida_login_cliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        usuario = Usuarios.objects.filter(email=email, senha=senha).first()

        if usuario:
            request.session['cliente'] = usuario.id
            return redirect('/edjane/index/')
        else:
            return redirect('/edjane/login/?status=1')

    return render(request, 'login.html')


def inicio(request):
    return render(request, 'pagina.html')

def emprestimo(request):
    return render(request, 'emprestimo.html')

def devolucao(request):
    return render(request, 'devolucao.html')


def user(request):
    return render(request, 'usuarios.html')

def livros(request):
    return render(request, 'livros.html')


def livros_mais_emprestados(request):
    # Agrupa os livros que foram emprestados e conta o número de vezes que foram emprestados
    livros = (Livros.objects
              .filter(emprestado=True)
              .values('nome')
              .annotate(total_emprestimos=Count('id'))
              .order_by('-total_emprestimos'))

    return render(request, 'emprestimo.html', {'livros_mais_emprestados': livros})


