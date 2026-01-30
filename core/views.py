from django.http import HttpResponse
from django.shortcuts import render


# Nossa lista global (Banco de Dados em memória)
chamados = [
    {"lab": "Lab 01", "problema": "PC lento", "prioridade": "Alta"},
    {"lab": "Lab 02", "problema": "Impressora sem tinta", "prioridade": "Média"},
    {"lab": "Lab 03", "problema": "Sem conexão com a internet", "prioridade": "Baixa"},
]

# Já retorna render
def home(request):
    return render(request, 'core/home.html')

# Ainda retorna HttpResponse
def criar(request, lab, problema, prioridade):
    # Criando o dicionário e adicionando à lista
    novo = {
        "lab": lab,
        "problema": problema,
        "prioridade": prioridade
    }
    chamados.append(novo)
    
    return HttpResponse(f"✅ Chamado para o {lab} criado com sucesso! <br> <a href='/'>Voltar</a>")

# Ainda retorna HttpResponse
def fechar(request, indice):
    del chamados[indice]
    
    return HttpResponse(f"✅ Chamado removido com sucesso! <br> <a href='/listar'>Voltar</a>")


# Já retorna render
def listar(request):
    return render(request, 'core/listar.html', {"chamados": chamados})
