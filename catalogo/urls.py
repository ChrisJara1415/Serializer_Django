from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.lista_categorias, name='lista-categorias'),
    path('productos/', views.lista_productos, name='lista-productos'),
    path('marcas/', views.lista_marcas, name='lista-marcas'),
]