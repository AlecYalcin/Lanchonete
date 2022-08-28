from .models        import Produto, Chefe
from django.forms   import ModelForm

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ["nome","preco","ingredientes","img_url"]

class ChefeForm(ModelForm):
    class Meta:
        model = Chefe
        fields = ["nome","posicao","img_url"]