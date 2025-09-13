from django.urls import path
from . import views

urlpatterns = [
    # Listar
    path('categorias/', views.lista_categorias, name='lista-categorias'),
    path('productos/', views.lista_productos, name='lista-productos'),
    path('marcas/', views.lista_marcas, name='lista-marcas'),

    # Detalles
    path("categorias/<int:pk>/", views.detalle_categoria, name='detalle_categoria'),
    path('productos/<int:pk>/', views.detalle_producto, name='detalle_producto'),
    path('marcas/<int:pk>/', views.detalle_marca, name='detalle_marca'),

    # CRUD Categorías
    path('categorias/crear/', views.crear_categoria, name='crear_categoría'),
    path('categorias/<int:pk>/actualizar', views.actualizar_categoria, name='actualizar_categoría'),
    path('categorias/<int:pk>/eliminar', views.eliminar_categoria, name='eliminar_categoría'),

    # CRUD Productos
    path('productos/crear', views.crear_producto, name='crear_producto'),
    path('productos/<int:pk>/actualizar', views.actualizar_producto, name='actualizar_producto'),
    path('productos/<int:pk>/eliminar', views.eliminar_producto, name='eliminar_producto'),
]