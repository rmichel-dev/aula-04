"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home, listar_chamados, novo_chamado, fechar_chamado, editar_chamado
from core.views import editar_categoria
from core.views import ListarCategoriasView, NovaCategoriaView, ExcluirCategoriaView
from core.views import api_chamados
urlpatterns = [
    # Exemplo de uso com FBV (Function Based View)
    path('admin/', admin.site.urls),
    path('', home),  # Deixando vazio '', a página aparece na raiz do site

    path('listar-chamados/', listar_chamados, name='listar-chamados'),
    path('editar-chamado/<int:id>', editar_chamado, name='editar-chamado'),
    path('novo-chamado/', novo_chamado),
    path('fechar-chamado/<int:id>', fechar_chamado, name='fechar-chamado'),
 
    path('editar-categoria/<int:id>', editar_categoria, name='editar-categoria'),

    # Exemplo de uso com CBV (class based view)
    path('listar-categorias', ListarCategoriasView.as_view(), name='listar-categorias'),
    path('nova-categoria', NovaCategoriaView.as_view(), name='nova-categoria'),
    path('excluir-categoria/<int:pk>', ExcluirCategoriaView.as_view(), name='excluir-categoria'),

    path('api/chamados/', api_chamados, name='listar-chamados-api'),
]