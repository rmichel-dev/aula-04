from django.http import HttpResponse
from django.shortcuts import render, redirect


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
def novoChamado(request): 
    # 1. Se o usuário clicou no botão de enviar (POST)
    if request.method == "POST":
        # Capturamos os dados do formulário
        laboratorio = request.POST.get('laboratorio')
        descricao = request.POST.get('descricao')
        prioridade = request.POST.get('prioridade')
        # Salvamos na nossa "base de dados"
        print(f"Recebido: {laboratorio}, {descricao}, {prioridade}") 

        chamados.append({
            "lab": laboratorio,
            "problema": descricao,
            "prioridade": prioridade
        })

        # 2. Redireciona de volta para a lista após salvar
        return redirect('/listar')

    # 3. Se o usuário apenas acessou a página (GET)
    return render(request, 'core/novo_chamado.html')
   

# Ainda retorna HttpResponse
def fechar(request, indice):
    del chamados[indice]
    
    return HttpResponse(f"✅ Chamado removido com sucesso! <br> <a href='/listar'>Voltar</a>")


# Já retorna render
def listar(request):
    return render(request, 'core/listar.html', {"chamados": chamados})
