from django.shortcuts import render, redirect, get_object_or_404
from .models import Chamado, Categoria
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from django.views.generic import CreateView, ListView, DeleteView, View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages

from django.http import JsonResponse

def home(request):
    return render(request, "core/home.html" ) 


# exemplo de view para criar um novo chamado
# Usando o método POST para receber os dados do formulário e criar um novo registro no banco de dados.
# Usando o método GET para exibir o formulário para o usuário.
def novo_chamado(request):
    if request.method == "POST":
        laboratorio = request.POST.get('laboratorio')
        descricao = request.POST.get('descricao')
        prioridade = request.POST.get('prioridade')
        id_categoria = request.POST.get('categoria')

        # Buscamos o objeto categoria no banco
        categoria_selecionada = Categoria.objects.get(id=id_categoria)

        Chamado.objects.create(
            laboratorio=laboratorio, 
            descricao=descricao, 
            prioridade=prioridade,
            categoria=categoria_selecionada # Passamos o objeto, não o texto!
        )
        
        messages.success(request, 'Chamado criado com sucesso!')
        return redirect('/listar-chamados')

    if request.method == "GET":
        print("chegou um get")
        categorias = Categoria.objects.all()
        return render(request, 'core/novo_chamado.html', {'categorias': categorias})


# recebemos o id do chamado que queremos fechar, 
# buscamos o chamado no banco de dados usando esse id 
# depois chamamos o método delete() para remover o registro do banco.


from django.contrib import messages
def fechar_chamado(request, id):
    chamado = Chamado.objects.get(id=id)
    chamado.delete()
    messages.success(request, 'Chamado fechado com sucesso')
    return redirect('/listar-chamados')


# primeiro decoramos a função com @login_required para garantir que o usuário esteja autenticado
# depois decoramos com @permission_required para verificar 
# se o usuário tem a permissão 'core.view_chamado' necessária para acessar essa view. 
# 
# Se o usuário NÃO tiver a permissão, será levantada uma exceção (raise_exception=True) 
@login_required
@permission_required('core.view_chamado', raise_exception=True) 
def listar_chamados(request):
    # Busca TODOS os registros do banco de dados
    chamados = Chamado.objects.all() 
    return render(request, 'core/listar_chamados.html', {"chamados": chamados})



# Neste exemplo, recebemos o id do chamado que queremos editar, buscamos o chamado no banco de dados usando esse id
# Para criarrmos o chamado precisamos passar também as categorias para o template, para que o usuário possa escolher a categoria do chamado.
# logo retornamos o objeto {'categorias': categorias, 'chamado': chamado}
def editar_chamado(request, id):
    # Busca TODOS os registros do banco de dados
    chamado = Chamado.objects.get(id=id)
    categorias = Categoria.objects.all()

    if request.method == "POST":
        # 2. Atualiza os campos com o que veio do formulário
        chamado.laboratorio = request.POST.get('laboratorio')
        chamado.descricao = request.POST.get('descricao')
        chamado.prioridade = request.POST.get('prioridade')
        id_cat = request.POST.get('categoria')

        chamado.categoria = Categoria.objects.get(id=id_cat)
        
        # 3. Salva as alterações
        chamado.save()
        return redirect('/listar-chamados')
    return render(request, 'core/editar_chamado.html', {'categorias': categorias, 'chamado': chamado,})

# Exmeplo de view para editar uma categoria, usando o id da categoria para buscar o registro no banco de dados,
# apenas usuários autenticados podem acessar essa view, por isso usamos o decorador @login_required
@login_required
def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == "POST":
        #salvar as alterações
        categoria.nome = request.POST.get('nome')
        categoria.save()
        return redirect('/listar-categorias')

    if request.method == "GET":
        #retornar o formulário preenchido com os dados atuais
        return render(request, 'core/editar_categoria.html', {'categoria': categoria})


# Exemplo de como era com FBV (function based view)
# def listar_categorias(request):
#     categorias = Categoria.objects.all() 
#     return render(request, 'core/listar_categorias.html', {"categorias": categorias})
#
# Exemplo de como fica com CBV (class based view)
class ListarCategoriasView(ListView):
    model = Categoria
    template_name = 'core/listar_categorias.html'
    context_object_name = 'categorias'

# Exemplo para criar uma nova categoria usando CBV (class based view)
# O usuário deve estar logado e ter a permissão 'core.add_categoria' para acessar essa view
# por isso usamos os mixins LoginRequiredMixin e PermissionRequiredMixin


class NovaCategoriaView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'core/nova_categoria.html'
    success_url = reverse_lazy('listar-categorias')

    permission_required = 'core.add_categoria'
    raise_exception = True




class ExcluirCategoriaView(LoginRequiredMixin, PermissionRequiredMixin, View):
    model = Categoria
    ## Caso quiséssemos usar um template para confirmar a exclusão, descomentariamos a linha abaixo e criaríamos o template 'core/confirmar_exclusao_categoria.html'
    # template_name = 'core/confirmar_exclusao_categoria.html'
    success_url = reverse_lazy('listar-categorias')

    permission_required = 'core.delete_categoria'
    raise_exception = True


    # Como não queremos usar um template para confirmar a exclusão, mudamos o mixing para get e não DeleteView
    # Sobrescrevemos o método get para chamar o método post diretamente, assim a exclusão acontece sem precisar de confirmação.
    def get(self, request, pk):
        categoria = get_object_or_404(Categoria, pk=pk)
        categoria.delete()
        return redirect(self.success_url)
    

def api_chamados(request):
    chamados = Chamado.objects.all()
    data = []
    for chamado in chamados:
        data.append({
            'id': chamado.id,
            'laboratorio': chamado.laboratorio,
            'descricao': chamado.descricao,
            'prioridade': chamado.prioridade,
            'categoria': chamado.categoria.nome,
        })
    return JsonResponse(data, safe=False)   