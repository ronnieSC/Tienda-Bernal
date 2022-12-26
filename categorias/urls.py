from django.contrib import admin
from django.urls import path
from .models import Categoria
from .views import Categoria_form, Categoria_ver, Categoria_edit

app_name="categorias"
urlpatterns = [
    path('add_categoria/', Categoria_form, name="Categoria_form"),
    path('ver_categorias/', Categoria_ver, name='Categoria_ver'),
    path('edit_categoria/<int:myID>/', Categoria_edit,name='Categoria_edit'),
]
