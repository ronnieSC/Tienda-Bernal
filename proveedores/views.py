from django.shortcuts import render, get_object_or_404, redirect

from django.contrib import messages

from .forms import ProveedorForm
from .models import Proveedor

# Create your views here.
def Proveedor_form(request):
	form=ProveedorForm()
	if request.method == 'POST':
		form=ProveedorForm(request.POST)
		if form.is_valid():
			Proveedor.objects.create(**form.cleaned_data)
			form=ProveedorForm()
			messages.info(request,'Proveedor Añadido con Exito')
	#else:
		#messages.info(request,'Error')
	context={
		'form':form
		}
	return render(request,'proveedores/proveedor_form.htm',context)

def Proveedor_view(request):
	if request.method=='POST':
		checked = request.POST.getlist('CHECKED')
		for ch in checked:
			obj=get_object_or_404(Proveedor, id=ch)
			obj.delete()
	proveedor=Proveedor.objects.all()
	context={
		'proveedor':proveedor,
		}
	return render(request,'proveedores/proveedor_view.htm',context)

def Proveedor_edit(request,myID):
	if request.method == 'POST':
		obj=get_object_or_404(Proveedor, id=myID)
		form=ProveedorForm(request.POST, request.FILES or None)
		if form.is_valid():
			Proveedor.objects.filter(id=myID).update(**form.cleaned_data)
			form=ProveedorForm()
			#messages.info(request,'Item Editado con Exito')
			return redirect('../../view_proveedor')
	else:
		obj=get_object_or_404(Proveedor, id=myID)
		initialvalues =obj.__dict__
		form=ProveedorForm(None,initial=initialvalues)
	
	context={
		'form':form
		}
	return render(request,'proveedor/proveedor_edit.htm',context)