from codecs import BOM
from django.db import models

# Create your models here.
class Adicional(models.Model):
    nome    = models.CharField(max_length=132)
    valor   = models.FloatField(default=0.0)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome    = models.CharField(max_length=132)
    valor   = models.FloatField(default=0.0)
    adc     = models.ForeignKey(Adicional, on_delete=models.CASCADE, default=1)
    bom     = models.BooleanField(default=False)


    