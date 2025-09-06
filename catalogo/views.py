from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import categoria, producto, marca
from .serializers import CategoriaSerializer, ProductoSerializer, MarcaSerializer

@api_view(['GET'])
def lista_categorias(request):
    categorias = categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def lista_productos(request):
    productos = producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def lista_marcas(request):
    marcas = marca.objects.all()
    serializer = MarcaSerializer(marcas, many=True)
    return Response(serializer.data)