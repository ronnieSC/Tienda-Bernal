from django.db import models
from django.urls import reverse

# Create your models here.
class Categoria(models.Model):
	CatNom=models.CharField(verbose_name="Nombre", max_length=100)
	CatImg=models.ImageField(verbose_name="Imagen", upload_to='pics/categorias',null=True) 

	def __str__(self):
		return self.CatNom

	def get_absolute_url(self):
		return reverse('categorias:Categoria_edit',kwargs={'myID':self.id})