from django.db import models

from clientes.models import Cliente
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Venta(models.Model):
	cliente=models.ForeignKey(Cliente, on_delete=models.CASCADE)
	vendedor=models.ForeignKey(User, on_delete=models.CASCADE)
	detalles=models.TextField()
	total=models.IntegerField()
	fecha= models.DateTimeField()

	def get_absolute_url(self):
		return reverse('venta:Venta_details',kwargs={'myID':self.id})