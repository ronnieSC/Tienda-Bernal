from django.db import models
from categorias.models import Categoria

class Producto(models.Model):
    productName = models.CharField(max_length=32)
    productDescription = models.CharField(max_length=64)
    productPrice = models.FloatField()
    productImage = models.ImageField(blank=True, null=True)
    productCategory = models.ForeignKey(to=Categoria, on_delete=models.DO_NOTHING)
