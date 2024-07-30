from django.shortcuts import render,get_object_or_404,redirect
from .models import Fornecedor,Produto,Entrada,Saida,Cliente
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import EntradaForm,SaidaForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.db.models import Q

def home(request):
    return render(request,"index.html")


#Criação de conta
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'login/cadastro.html', {'form': form})


#Clientes

class Listar_Clientes(LoginRequiredMixin,ListView):
    model = Cliente
    template_name = "clientes/listar_clientes.html"
    context_object_name = "clientes"
    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.GET.get('q', '')  # Pega o termo de pesquisa, padrão é uma string vazia
        
        if search_term:
            queryset = queryset.filter(
                Q(nome__icontains=search_term) |  # Filtra pelo nome do produto
                Q(email__icontains=search_term)  # Filtra pela descrição do produto (opcional)
            )
        
        return queryset

class Criar_Cliente(LoginRequiredMixin,CreateView):
    model = Cliente
    template_name = "clientes/cliente_form.html"
    fields = ["nome", "telefone", "email"]
    success_url = reverse_lazy("Listar_clientes")


class Atualizar_Cliente(LoginRequiredMixin,UpdateView):
    model = Cliente
    template_name = "clientes/cliente_form.html"
    fields = ["nome", "telefone", "email"]
    success_url = reverse_lazy("Listar_clientes")


class Deletar_Cliente(LoginRequiredMixin,DeleteView):
    model = Cliente
    template_name = "clientes/deletar_cliente.html"
    success_url = reverse_lazy("Listar_clientes")

@login_required
def detalhes_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, "clientes/cliente_detalhes.html", {"cliente": cliente})



#Fornecedores


class Listar_Fornecedores(LoginRequiredMixin,ListView):
    model = Fornecedor
    template_name = "fornecedores/listar_fornecedores.html"
    context_object_name = "fornecedores"
    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.GET.get('q', '')  # Pega o termo de pesquisa, padrão é uma string vazia
        
        if search_term:
            queryset = queryset.filter(
                Q(nome__icontains=search_term) |  # Filtra pelo nome do produto
                Q(resumo__icontains=search_term)  # Filtra pela descrição do produto (opcional)
            )
        
        return queryset

class Criar_Fornecedor(LoginRequiredMixin,CreateView):
    model = Fornecedor
    template_name = "fornecedores/fornecedor_form.html"
    fields = ["nome", "telefone", "email", "resumo"]
    success_url = reverse_lazy("Listar_fornecedores")


class Atualizar_Fornecedor(LoginRequiredMixin,UpdateView):
    model = Fornecedor
    template_name = "fornecedores/fornecedor_form.html"
    fields = ["nome", "telefone", "email", "resumo"]
    success_url = reverse_lazy("Listar_fornecedores")


class Deletar_Fornecedor(LoginRequiredMixin,DeleteView):
    model = Fornecedor
    template_name = "fornecedores/deletar_fornecedor.html"
    success_url = reverse_lazy("Listar_fornecedores")

@login_required
def detalhes_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    return render(request, "fornecedores/fornecedor_detalhes.html", {"fornecedor": fornecedor})

#Produtos

class Listar_Produtos(LoginRequiredMixin,ListView):
    model = Produto
    template_name = "estoque/produtos_list.html"
    context_object_name = "produtos"

    def get_queryset(self):
        queryset = super().get_queryset()
        search_term = self.request.GET.get('q', '')  # Pega o termo de pesquisa, padrão é uma string vazia
        
        if search_term:
            queryset = queryset.filter(
                Q(nome__icontains=search_term) |  # Filtra pelo nome do produto
                Q(descricao__icontains=search_term)  # Filtra pela descrição do produto (opcional)
            )
        
        return queryset
        
class Criar_Produto(LoginRequiredMixin,CreateView):
    model = Produto
    template_name = "estoque/produto_form.html"
    fields = ["nome","fornecedor","quantidade","valor_compra","valor_venda","descricao"]
    success_url=reverse_lazy("Listar_produtos")


class Atualizar_Produto(LoginRequiredMixin,UpdateView):
    model = Produto
    template_name = "estoque/produto_form.html"
    fields = ["nome","fornecedor","quantidade","valor_compra","valor_venda","descricao"]
    success_url = reverse_lazy("Listar_produtos")


class Deletar_Produto(LoginRequiredMixin,DeleteView):
    model = Produto
    template_name = "estoque/deletar_produto.html"
    success_url = reverse_lazy("Listar_produtos")

@login_required
def detalhes_produto(request,pk):
    produto = get_object_or_404(Produto,pk=pk)
    return render(request,"estoque/produtos_detalhes.html",{"produto":produto})

@login_required
def registrar_entrada(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.produto = produto
            entrada.save()
            produto.quantidade += entrada.quantidade
            produto.save()
            return redirect('Listar_produtos')
    else:
        form = EntradaForm()
    return render(request, 'estoque/entrada_produto.html', {'form': form, 'produto': produto})

@login_required
def registrar_saida(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = SaidaForm(request.POST)
        if form.is_valid():
            saida = form.save(commit=False)
            saida.produto = produto
            if produto.quantidade >= saida.quantidade:
                saida.save()
                produto.quantidade -= saida.quantidade
                produto.save()
                return redirect('Listar_produtos')
            else:
                form.add_error('quantidade', 'Quantidade insuficiente em estoque.')
    else:
        form = SaidaForm()
    return render(request, 'estoque/saida_produto.html', {'form': form, 'produto': produto})

@login_required
def listar_entradas(request):
    query = request.GET.get('q')
    if query:
        entradas = Entrada.objects.filter(produto__nome__icontains=query).order_by('-data')
    else:
        entradas = Entrada.objects.all().order_by('-data')
    return render(request, 'estoque/listar_entradas.html', {'entradas': entradas})

@login_required
def listar_saidas(request):
    query = request.GET.get('q')
    if query:
        saidas = Saida.objects.filter(produto__nome__icontains=query).order_by('-data')
    else:
        saidas = Saida.objects.all().order_by('-data')
    return render(request, 'estoque/listar_saidas.html', {'saidas': saidas})