from .models        import Produto, Adicional
from django.forms   import ModelForm

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ["nome","valor","adc","bom"]