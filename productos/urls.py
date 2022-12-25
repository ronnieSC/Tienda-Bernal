from django.urls import path
from . import views

urlpatterns = [
    path('all', views.productsAllView),
    path('update/<int:id>', views.productsUpdateView),
    path('read/<int:id>', views.productsReadView),
    path('create/', views.productsCreateView),
]