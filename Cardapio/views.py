from django.shortcuts import render, redirect
from django.http      import HttpResponse
from Cardapio.form    import ProdutoForm
from Cardapio.models  import Produto
# Create your views here.

def index(request):
    # Pegar todos os PRODUTOS.
    cardapio = Produto.objects.all()
    produtos = {"produtos_chave": cardapio}
    return render(request, "index.html", produtos)

def createProduto(request):
    # Criação de FORMULÁRIO do Produto
    form = ProdutoForm(request.POST or None)
    # Varificar se o FORMULÁRIO é VÁLIDO
    if form.is_valid():
        form.save()
        return redirect("createProduto")
    # Retornar tudo para createProduto.html
    produtos = {"form_produto": form}
    return render(request, "createProduto.html", produtos)

def updateProduto(request, id_produto):
    # Pegar o PRODUTO específico
    produto = Produto.objects.get(pk=id_produto)
    # Criação de FORMULÁRIO do PRODUTO específico
    form = ProdutoForm(request.POST or None, instance=produto)
    # Verificação de FORMULÁRIO
    if form.is_valid():
        form.save()
        return redirect("main")
    # Retornar tudo para createProduto.html
    produtos = {"form_produto": form}
    return render(request, "createProduto.html", produtos)

def deleteProduto(request, id_produto):
    # Pegar o PRODUTO específico
    produto = Produto.objects.get(pk = id_produto)
    # Deletar o PRODUTO
    produto.delete()
    # Voltar para o index.html
    return redirect("main")