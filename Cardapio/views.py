from django.shortcuts import render, redirect
from django.http      import HttpResponse
from Cardapio.form    import ProdutoForm, ChefeForm
from Cardapio.models  import Produto, Chefe
# Create your views here.

def index(request):
    # Pegar todos os PRODUTOS.
    cardapio = Produto.objects.all()
    chefes   = Chefe.objects.all()
    produtos = {"produtos_chave": cardapio, "chefes_chave": chefes}
    return render(request, "index.html", produtos)

# ==================================================================================
# CRUD de PRODUTO
# ==================================================================================
def createProduto(request):
    # Criação de FORMULÁRIO do Produto
    form = ProdutoForm(request.POST or None)
    # Varificar se o FORMULÁRIO é VÁLIDO
    if form.is_valid():
        form.save()
        return redirect("main")
    # Retornar tudo para createProduto.html
    produtos = {"form_produto": form}
    return render(request, "produto.html", produtos)

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
    return render(request, "produto.html", produtos)

def deleteProduto(request, id_produto):
    # Pegar o PRODUTO específico
    produto = Produto.objects.get(pk = id_produto)
    # Deletar o PRODUTO
    produto.delete()
    # Voltar para o index.html
    return redirect("main")

# ==================================================================================
# CRUD de Chefe
# ==================================================================================
def createChefe(request):
    # Criar FORMULÁRIO do CHEFE
    form = ChefeForm(request.POST or None)
    # Verificação de Formulário
    if form.is_valid():
        form.save()
        return redirect("main")
    # Retornar tudo para createChefe.html
    chefes = {"form_chefe": form}
    return render(request, "chefe.html", chefes)

def updateChefe(request, id_chefe):
    # Pegar o Chefe específico
    chefe = Chefe.objects.get(pk=id_chefe)
    # Criação de FORMULÁRIO do Chefe específico
    form = ChefeForm(request.POST or None, instance=chefe)
    # Verificação de FORMULÁRIO
    if form.is_valid():
        form.save()
        return redirect("main")
    # Retornar tudo para createChefe.html
    chefes = {"form_chefe": form}
    return render(request, "chefe.html", chefes)

def deleteChefe(request, id_chefe):
    chefe = Chefe.objects.get(pk=id_chefe)
    chefe.delete()
    return redirect("main")