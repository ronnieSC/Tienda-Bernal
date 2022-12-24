from django.db import models

# Create your models here.
class Categoria(models.Model):
	CatNom		= models.CharField(verbose_name='Nombre de la categoría', max_length=50)
	#CatImg		= models.ImageField(verbose_name='Imagen', upload_to='pics/categories', null=True, blank=True)

	def __str__(self):
		return self.CatNom
