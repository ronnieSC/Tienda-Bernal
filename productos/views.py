from django.shortcuts import render, redirect
from .models import Producto
from categorias.models import Categoria

def productsAllView(request):
    productos = Producto.objects.all()
    return render(request, "all.html", {"productos":productos})

def productsCreateView(request):
    if request.method == 'POST':
        # Getting values
        productName = request.POST['name']
        productDescription = request.POST['description']
        productPrice = float(request.POST['price'].replace(",","."))
        productCategory = request.POST['category']
        productImage = request.FILES['image']

        # Creating object
        prod = Producto.objects.create(
            productName=productName,
            productDescription=productDescription,
            productPrice=productPrice,
            productCategory=Categoria.objects.get(id=productCategory),
            productImage=productImage
        )
        prod.save()
        # If it's OK -> save -> redirect
        return redirect('/productos/all')

    categories = Categoria.objects.all() 
    return render(request, "create.html", {"categories":categories})

def productsReadView(request, id):
    product = Producto.objects.get(id=id)
    return render(request, "read.html", {"product": product})

def productsUpdateView(request, id):
    if request.method == 'POST':

        # Getting values
        productName = request.POST['name']
        productDescription = request.POST['description']
        productPrice = float(request.POST['price'].replace(",","."))
        productCategory = request.POST['category']
        productImage = request.FILES['image']

        # Updating object
        prod = Producto.objects.filter(id=id).update(
            productName=productName,
            productDescription=productDescription,
            productPrice=productPrice,
            productCategory=Categoria.objects.get(id=productCategory),
            productImage=productImage
        )

        productos = Producto.objects.all()
        return redirect(to="/productos/all")

    product = Producto.objects.get(id=id)
    categories = Categoria.objects.all()
    return render(request, "update.html", {"product":product, "categories":categories})
