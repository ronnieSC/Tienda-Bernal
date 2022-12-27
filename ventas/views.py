from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from clientes.models import Cliente
from django.contrib.auth.models import User
from productos.models import Producto
from .models import Venta

import datetime

# Create your views here.
def Venta_form(request):
	if request.method=='POST':
		if (verify_fields(request=request)==False):
			messages.info(request,'Error en los datos ingresados')
			return render(request,'ventas/venta_form.htm',{}) 
		if (verify_existences(request=request)==False):
			messages.info(request,'Existencias agotadas o valores repetidos en la lista')
			return render(request,'ventas/venta_form.htm',{}) 
		i=0
		detalles="<tr>\n<th>Nombre</th><th>Descripción</th><th>Cantidad</th><th>Precio</th>\n</tr>\n"
		cliente=get_object_or_404(Cliente, id=request.POST.getlist('cliente')[0])
		vendedor=get_object_or_404(User, id=request.user.id)
		prod_id = request.POST.getlist('txtprecio')
		for ch in prod_id:
			producto=get_object_or_404(Producto, id=request.POST.getlist('cboxproducto')[i])
			detalles+="<tr>\n"
			detalles+="<td>"+producto.nombre+"</td>"+"<td>"+request.POST.getlist('txtdescripcion')[i]+"</td>"
			detalles+="<td>"+request.POST.getlist('cboxcantidad')[i]+"</td>"+"<td>"+request.POST.getlist('txtprecio')[i]+"</td>\n"
			detalles+="</tr>\n"
			i+=1
		total=request.POST.getlist('total')[0]
		today = datetime.now()
		fecha=today
		i=0
		pid = request.POST.getlist('cboxproducto')
		for ch in pid:
			obj=get_object_or_404(Producto, id=ch)
			Producto.objects.filter(id=ch).update(cantidad=int(obj.cantidad)-int(request.POST.getlist('cboxcantidad')[i]))
			i+=1
		venta=Venta(cliente=cliente, vendedor=vendedor, detalles=detalles, total=total, fecha=fecha)
		venta.save()
		messages.info(request,'Item Añadido con Exito')
	return render(request,'ventas/venta_form.htm',{})

def verify_fields(request):
	client_fields = ["cliente", "DNI", "txtdireccion","txtemail","txttelefono"]
	for x in client_fields:
		if (request.POST.getlist(x)[0]==""):
			return False
	i=0
	pre = request.POST.getlist('txtprecio')
	for ch in pre:
		if (request.POST.getlist('cboxproducto')[i]=="" or request.POST.getlist('cboxproducto')[i]=="0"):
			return False
		if (request.POST.getlist('txtdescripcion')[i]=="" or request.POST.getlist('txtdescripcion')[i]=="0" ):
			return False
		if (request.POST.getlist('cboxcantidad')[i]=="" or request.POST.getlist('cboxcantidad')[i]=="0" ):
			return False
		if (request.POST.getlist('txtprecio')[i]=="" or request.POST.getlist('txtprecio')[i]=="0" ):
			return False
		i+=1
	return True

def verify_existences(request):
	i=0
	prod_id = request.POST.getlist('cboxproducto')
	if (len(prod_id) != len(set(prod_id))):
		return False
	for ch in prod_id:
		obj=get_object_or_404(Producto, id=ch)
		if (int(obj.cantidad)-int(request.POST.getlist('cboxcantidad')[i])<0):
			return False
		i+=0
	return True