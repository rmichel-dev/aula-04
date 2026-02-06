from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Chamado, Categoria
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "core/home.html" ) 

#@login_required
def novo_chamado(request):
    if request.method == "POST":
        laboratorio = request.POST.get('laboratorio')
        descricao = request.POST.get('descricao')
        prioridade = request.POST.get('prioridade')

        Chamado.objects.create(laboratorio=laboratorio, descricao=descricao, prioridade=prioridade)
        return redirect('/listar-chamados')

    if request.method == "GET":
        print("chegou um get")
        return render(request, 'core/novo_chamado.html')

# Ainda retorna HttpResponse
def fechar_chamado(request, id):
    chamado = Chamado.objects.get(id=id)
    chamado.delete()
    print(f"Fechando chamado {chamado.id} - {chamado.descricao}")
    return redirect('/listar-chamados')

#@login_required
def listar_chamados(request):
    # Busca TODOS os registros do banco de dados
    chamados = Chamado.objects.all() 
    return render(request, 'core/listar-chamados.html', {"chamados": chamados})



# Novas views para categorias
# @login_required
def listar_categorias(request):
    categorias = Categoria.objects.all() 
    return render(request, 'core/listar_categorias.html', {"categorias": categorias})

def nova_categoria(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        Categoria.objects.create(nome=nome)
        # salvar meus dados
        return redirect('/listar-categorias')
    return render(request, 'core/nova_categoria.html')

def excluir_categoria(request, id):
    Categoria.objects.get(id=id).delete()
    return redirect('/listar-categorias')