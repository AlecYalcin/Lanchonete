from django.db import models

# Create your models here.
class Produto(models.Model):
    nome            = models.CharField(max_length=132)
    preco           = models.FloatField(default=0.0)
    ingredientes    = models.CharField(max_length=300)
    img_url         = models.CharField(max_length=999, default="https://cdn.discordapp.com/attachments/822156056460394619/1014589119600533575/unknown.png")

class Chefe(models.Model):
    nome            = models.CharField(max_length=132)
    posicao         = models.CharField(max_length=100)
    img_url         = models.CharField(max_length=999, default='https://cdn.discordapp.com/attachments/822156056460394619/1014589119600533575/unknown.png')
