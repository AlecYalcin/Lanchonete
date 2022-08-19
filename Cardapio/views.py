from django.shortcuts import render, redirect
from django.http      import HttpResponse
from Cardapio.form    import ProdutoForm
from Cardapio.models  import Produto, Adicional
# Create your views here.

def index(request):
    cardapio = Produto.objects.all()
    
    for i in cardapio:
        adicional = Adicional.objects.get(pk=i.adc)
        i.adicional.update({"oii": adicional.nome})
    
    
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("cardapio")
    produtos = {"produtos_chave": cardapio, "form_produto": form}
    return render(request, "index.html", produtos)

def update(request, id_produto):
    produto = Produto.objects.get(pk=id_produto)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect("cardapio")
    produtos = {"form_produto": form}
    return render(request, "index.html", produtos)