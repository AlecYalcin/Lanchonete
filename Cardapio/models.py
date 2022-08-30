from django.db import models

# Create your models here.
class Produto(models.Model):
    nome            = models.CharField(max_length=132)
    preco           = models.FloatField(default=0.0)
    ingredientes    = models.CharField(max_length=300)
    img_url         = models.CharField(max_length=999)

class Chefe(models.Model):
    nome            = models.CharField(max_length=132)
    posicao         = models.CharField(max_length=100)
    img_url         = models.CharField(max_length=999, default='https://pbs.twimg.com/profile_images/1265738409810722816/cLkZUf3f_400x400.jpg')
