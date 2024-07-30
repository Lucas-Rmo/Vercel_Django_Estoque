from django.urls import path
from .views import *

urlpatterns = [
    #path("",,name="home")
    path("",home,name="home"),
    #Produtos
    path("Produtos/",Listar_Produtos.as_view(),name="Listar_produtos"),
    path("Produtos/Cadastro",Criar_Produto.as_view(),name="Cadastro_produto"),
    path("Produtos/Editar/<int:pk>/",Atualizar_Produto.as_view(),name="Editar_produto"),
    path("Produtos/Excluir/<int:pk>/",Deletar_Produto.as_view(),name="Deletar_produto"),
    path("Produtos/Detalhes/<int:pk>/",detalhes_produto,name="Detalhes_produto"),
    path('Produtos/Entrada/<int:pk>/', registrar_entrada, name='registrar_entrada'),
    path('Produtos/Saida/<int:pk>/', registrar_saida, name='registrar_saida'),
    path('Produtos/Historico/Entradas/', listar_entradas, name='listar_entradas'),
    path('Produtos/Historico/Saidas/', listar_saidas, name='listar_saidas'),

    #Fornecedores
    path("Fornecedores/",Listar_Fornecedores.as_view(),name="Listar_fornecedores"),
    path("Fornecedores/Cadastro",Criar_Fornecedor.as_view(),name="Cadastro_fornecedor"),
    path("Fornecedores/Excluir/<int:pk>/",Deletar_Fornecedor.as_view(),name="Deletar_fornecedor"),
    path("Fornecedores/Editar/<int:pk>/",Atualizar_Fornecedor.as_view(),name="Editar_fornecedor"),
    path("Fornecedores/Detalhes/<int:pk>/",detalhes_fornecedor,name="Detalhes_fornecedor"),

    
    #Clientes
    path("Clientes/", Listar_Clientes.as_view(), name="Listar_clientes"),
    path("Clientes/Cadastro", Criar_Cliente.as_view(), name="Cadastro_cliente"),
    path("Clientes/Excluir/<int:pk>/", Deletar_Cliente.as_view(), name="Deletar_cliente"),
    path("Clientes/Editar/<int:pk>/", Atualizar_Cliente.as_view(), name="Editar_cliente"),
    path("Clientes/Detalhes/<int:pk>/", detalhes_cliente, name="Detalhes_cliente"),
]   