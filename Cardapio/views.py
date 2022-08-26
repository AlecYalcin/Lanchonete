from django.shortcuts import render, redirect
from django.http      import HttpResponse
from Cardapio.form    import ProdutoForm
from Cardapio.models  import Produto, Adicional
# Create your views here.

def index(request):
    cardapio = Produto.objects.all().values
    adicional = Adicional.objects.all().values

    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("cardapio")
    produtos = {"produtos_chave": cardapio, "adicional_chave": adicional,"form_produto": form}
    return render(request, "index.html", produtos)

def update(request, id_produto):
    produto = Produto.objects.get(pk=id_produto)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect("cardapio")
    produtos = {"form_produto": form}
    return render(request, "index.html", produtos)

def delete(request, id_produto):
    mesa = Produto.objects.get(pk = id_produto)
    mesa.delete()
    return redirect("cardapio")