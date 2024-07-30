from django.db import models

# Create your models here.

class Fornecedor(models.Model):

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=25,blank=True)
    email = models.EmailField(blank=True)
    resumo = models.TextField(blank=True)

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"

    def __str__(self):
        return self.nome
    
class Cliente(models.Model):

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=25,blank=True)
    email = models.EmailField(blank=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return self.nome

    
class Produto(models.Model):

    nome = models.CharField(max_length=100)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valor_compra = models.FloatField()
    valor_venda = models.FloatField()
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Entrada(models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)

class Saida(models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)


