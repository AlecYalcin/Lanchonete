from .models        import Produto, Chefe
from django.forms   import ModelForm

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ["nome","preco","ingredientes","img_url"]
        labels = {
            'nome': ('Nome do Prato'), 
            'preco': ('Preço do Prato'), 
            'ingredientes': ('Ingredientes'), 
            'img_url': ('Imagem URL')
        }

class ChefeForm(ModelForm):
    class Meta:
        model = Chefe
        fields = ["nome","posicao","img_url"]
        labels = {
            'nome': ('Nome do Funcionário'), 
            'posicao': ('Posição na Cozinha'), 
            'img_url': ('Imagem URL')
        }
