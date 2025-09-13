from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import categoria, producto, marca
from .serializers import CategoriaSerializer, ProductoSerializer, MarcaSerializer
from django.shortcuts import get_object_or_404

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

# Endpoints 13/09/2025

@api_view(["GET"])
def detalle_categoria(request, pk):
    #Buscamos la categoría por ID
    categoria = get_object_or_404(categoria, pk=pk)
    #Serializamos el objeto encontrado
    serializer = CategoriaSerializer(categoria)
    #Devolvemos el objeto como JSON
    return Response(serializer.data, status=status.HTTP_200_OK)

# Endpoint para obtener el detalle de un producto
@api_view(["GET"])
def detalle_producto(request, pk):
    #Buscamos el producto por ID
    producto = get_object_or_404(producto, pk)
    #Serializamos el producto
    serializer = ProductoSerializer(producto)
    #Devolvemos el producto como JSON
    return Response(serializer.data, status=status.HTTP_200_OK)