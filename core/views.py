from django.http import HttpResponse
from django.shortcuts import render, redirect


# Nossa lista global (Banco de Dados em memória)
chamados = [
    {"id": 1, "laboratorio": "Lab 01", "descricao": "PC lento", "prioridade": "Alta"},
    {"id": 2, "laboratorio": "Lab 02", "descricao": "Impressora sem tinta", "prioridade": "Média"},
    {"id": 3, "laboratorio": "Lab 03", "descricao": "Sem conexão com a internet", "prioridade": "Baixa"},
]

# Novas listas globais para categorias
categorias = [
    {"id": 1, "nome": "Hardware"},
    {"id": 2, "nome": "Software"},
    {"id": 3, "nome": "Rede"},
]

def home(request):
    return render(request, 'core/home.html')

def novo_chamado(request): 
    # 1. Se o usuário clicou no botão de enviar (POST)
    if request.method == "POST":
        # Capturamos os dados do formulário
        laboratorio = request.POST.get('laboratorio')
        descricao = request.POST.get('descricao')
        prioridade = request.POST.get('prioridade')
        # Salvamos na nossa "base de dados"
        print(f"Recebido: {laboratorio}, {descricao}, {prioridade}") 

        chamados.append({
            "id": len(chamados) + 1,
            "laboratorio": laboratorio,
            "descricao": descricao,
            "prioridade": prioridade
        })

        # 2. Redireciona de volta para a lista após salvar
        return redirect('/listar')

    # 3. Se o usuário apenas acessou a página (GET)
    return render(request, 'core/novo_chamado.html')
   

def fechar(request, id):
    for chamado in chamados:
        if chamado["id"] == id:
            chamados.remove(chamado)
            break
    
    return redirect('/listar')

def listar_chamados(request):
    return render(request, 'core/listar.html', {"chamados": chamados})




# Novas views para categorias

def listar_categorias(request):
    return render(request, 'core/listar_categorias.html', {"categorias": categorias})

def nova_categoria(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        categorias.append({
            "id": len(categorias) + 1,
            "nome": nome
        })
        # salvar meus dados
        return redirect('/listar-categorias')
    return render(request, 'core/nova_categoria.html')

def excluir_categoria(request, id):
    for categoria in categorias:
        if categoria["id"] == id:
            categorias.remove(categoria)
            break
    return redirect('/listar-categorias')