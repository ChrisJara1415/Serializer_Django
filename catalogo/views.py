from rest_framework import viewsets
from .models import Categoria, Producto, Marca
from .serializers import CategoriaSerializer, ProductoSerializer, MarcaSerializer

# ---------------------------------
# ViewSet para categoría
# ---------------------------------

class CategoriaViewSet(viewsets.ModelViewSet):
    """
    ViewSet que gestiona automáticamente:
    - listar (GET /categorias)
    - Detalle (GET /categorias/{id}/)
    - Crear (POST /categorias)
    - Actualizar (PUT /categorias{id}/)
    - Eliminar (DELETE /categorias/{id}/)
    """
    queryset = Categoria.objects.all() #definimos el conjunto de datos
    serializer_class = CategoriaSerializer #Definimos el serializador a usar
    
# ---------------------------------
# ViewSet para Producto
# ---------------------------------

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
# ---------------------------------
# ViewSet para Marca
# ---------------------------------    

class MarcaViewSet(viewsets.ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer