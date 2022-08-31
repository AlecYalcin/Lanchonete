from django.shortcuts import render, redirect
from django.http      import HttpResponse
from Cardapio.form    import ProdutoForm, ChefeForm
from Cardapio.models  import Produto, Chefe

def index(request):
    cardapio = Produto.objects.all()
    chefes   = Chefe.objects.all()
    produtos = {"produtos_chave": cardapio, "chefes_chave": chefes}
    return render(request, "index.html", produtos)

# ==================================================================================
# CRUD de PRODUTO
# ==================================================================================
def createProduto(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    produtos = {"form_produto": form}
    return render(request, "produto.html", produtos)

def updateProduto(request, id_produto):
    produto = Produto.objects.get(pk=id_produto)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect("main")
    produtos = {"form_produto": form}
    return render(request, "produto.html", produtos)

def deleteProduto(request, id_produto):
    produto = Produto.objects.get(pk = id_produto)
    produto.delete()
    return redirect("main")

# ==================================================================================
# CRUD de Chefe
# ==================================================================================
def createChefe(request):
    form = ChefeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("main")
    chefes = {"form_chefe": form}
    return render(request, "chefe.html", chefes)

def updateChefe(request, id_chefe):
    chefe = Chefe.objects.get(pk=id_chefe)
    form = ChefeForm(request.POST or None, instance=chefe)
    if form.is_valid():
        form.save()
        return redirect("main")
    chefes = {"form_chefe": form}
    return render(request, "chefe.html", chefes)

def deleteChefe(request, id_chefe):
    chefe = Chefe.objects.get(pk=id_chefe)
    chefe.delete()
    return redirect("main")