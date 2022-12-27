from django.urls import path
from .views import Proveedor_form,Proveedor_view,Proveedor_edit

app_name="proveedor"
urlpatterns = [
	path('add_proveedor/', Proveedor_form,name="Proveedor_form"),
    path('view_proveedor/', Proveedor_view,name="Proveedor_view"),
    path('edit_proveedor/<int:myID>/', Proveedor_edit,name='Proveedor_edit'),
]