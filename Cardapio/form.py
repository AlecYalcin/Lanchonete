from .models        import Produto
from django.forms   import ModelForm

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ["nome","preco","ingredientes","img_url"]