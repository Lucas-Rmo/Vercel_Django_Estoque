from django import forms 
from .models import Produto,Entrada,Saida,Fornecedor
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FornecedorForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ["nome","telefone","email","resumo"]

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ["nome","fornecedor","quantidade","valor_compra","valor_venda","descricao"]


class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ["quantidade"]

class SaidaForm(forms.ModelForm):
    class Meta:
        model = Saida
        fields = ["quantidade","cliente"]



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']