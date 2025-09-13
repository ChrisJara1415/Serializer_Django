from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.lista_categorias, name='lista-categorias'),
    path('productos/', views.lista_productos, name='lista-productos'),
    path('marcas/', views.lista_marcas, name='lista-marcas'),
    path("categorias/<int:pk>/", views.detalle_categoria, name='detalle_categoria'),
    path('productos/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('marcas/<int:pk>/', views.detalle_marca, name='detalle_marca')
]