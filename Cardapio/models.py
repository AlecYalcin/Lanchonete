from codecs import BOM
from django.db import models

# Create your models here.
class Produto(models.Model):
    nome            = models.CharField(max_length=132)
    preco           = models.FloatField(default=0.0)
    ingredientes    = models.CharField(max_length=300)
    img_url         = models.CharField(max_length=999)