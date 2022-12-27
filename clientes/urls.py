from django.urls import path
from .views import ClienteCreateView, ClienteListView, ClienteDetailView, ClienteUpdateView, ClienteDeleteView, ClienteQueryView

app_name='clientes'

urlpatterns = [
    path('create/',ClienteCreateView.as_view(),name='cliente-create'),
    path('',ClienteListView.as_view(),name='cliente-list'),
    path('<int:pk>/',ClienteDetailView.as_view(),name='cliente-detail'),
    path('<int:pk>/update/',ClienteUpdateView.as_view(),name='cliente-update'),
    path('<int:pk>/delete/',ClienteDeleteView.as_view(),name='cliente-delete'),
    path('query/',ClienteQueryView.as_view(),name='cliente-query'),
]