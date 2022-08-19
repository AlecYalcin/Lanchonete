from django.shortcuts import render
from django.http      import HttpResponse
from Cardapio.form    import ProdutoForm
from Cardapio.models  import Produto, Adicional
# Create your views here.

def index(request):
    cardapio = Produto.objects.all().values
    form = ProdutoForm()
    produtos = {"produtos_chave": cardapio, "produtos_value": 20, "form_produto": form}
    return render(request, "index.html", produtos)