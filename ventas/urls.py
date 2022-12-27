from django.urls import path
from .views import Venta_form

app_name="venta"
urlpatterns = [
    path('formulario_venta/', Venta_form,name="Venta_form"),
]