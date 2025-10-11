from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoriaViewSet, ProductoViewSet, MarcaViewSet, registro, login, logout

#Creamos el router
router = DefaultRouter()

#Registramos los ViewSets en el router
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'marcas', MarcaViewSet)

#Ahora las rutas se generan automáticamente
urlpatterns = [
    path('', include(router.urls)),
    path('registro/', registro, name='registro'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]