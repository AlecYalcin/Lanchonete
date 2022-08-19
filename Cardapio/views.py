from django.shortcuts import render, redirect
from django.http      import HttpResponse
from Cardapio.form    import ProdutoForm
from Cardapio.models  import Produto, Adicional
# Create your views here.

def index(request):
    cardapio = Produto.objects.all().values
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("cardapio")
    produtos = {"produtos_chave": cardapio, "form_produto": form}
    return render(request, "index.html", produtos)