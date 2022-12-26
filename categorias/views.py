from django.shortcuts import render, get_object_or_404, redirect

from .forms import CategoriaForm
from .models import Categoria

# Create your views here.
def Categoria_form(request):
	if request.method == 'POST':
		form=CategoriaForm(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			form=CategoriaForm()
	else:
		form = CategoriaForm()
	
	context={
		'form':form
		}
	return render(request,'categorias/categoria_form.htm',context)

def Categoria_ver(request):
    if request.method=='POST':
        checked = request.POST.getlist('CHECKED')

        for ch in checked:
            obj = get_object_or_404(Categoria, id=ch)
            obj.delete()

    categorias = Categoria.objects.all()

    context={
        'categorias': categorias,
    }

    return render(request, 'categorias/categorias_ver.htm', context)

def Categoria_edit(request,myID):
	if request.method == 'POST':
		obj=get_object_or_404(Categoria, id=myID)
		form=CategoriaForm(request.POST, request.FILES or None,instance=obj)
		if form.is_valid():
			form.save()
			#messages.info(request,'Item Editado con Exito')
			return redirect('../../ver_categorias')
	else:
		obj=get_object_or_404(Categoria, id=myID)
		form = CategoriaForm(instance=obj)
	
	context={
		'form':form
		}
	return render(request,'categorias/categoria_edit.htm',context)