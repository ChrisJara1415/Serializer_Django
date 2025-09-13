from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Categoria, Producto, Marca
from .serializers import CategoriaSerializer, ProductoSerializer, MarcaSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def lista_categorias(request):
    categorias = Categoria.objects.all()
    serializer = CategoriaSerializer(categorias, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def lista_productos(request):
    productos = Producto.objects.all()
    serializer = ProductoSerializer(productos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def lista_marcas(request):
    marcas = Marca.objects.all()
    serializer = MarcaSerializer(marcas, many=True)
    return Response(serializer.data)

# Endpoints 13/09/2025

@api_view(["GET"])
def detalle_categoria(request, pk):
    #Buscamos la categoría por ID
    categoria = get_object_or_404(Categoria, pk=pk)
    #Serializamos el objeto encontrado
    serializer = CategoriaSerializer(categoria)
    #Devolvemos el objeto como JSON
    return Response(serializer.data, status=status.HTTP_200_OK)

# Endpoint para obtener el detalle de un producto
@api_view(["GET"])
def detalle_producto(request, pk):
    #Buscamos el producto por ID
    producto = get_object_or_404(Producto, pk=pk)
    #Serializamos el producto
    serializer = ProductoSerializer(producto)
    #Devolvemos el producto como JSON
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def detalle_marca(request, pk):
    marca = get_object_or_404(Marca, pk=pk)
    serializer = MarcaSerializer(marca)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def crear_categoria(request):
    #Creamos un serializer con los datos enviados en la petición
    serializer = CategoriaSerializer(data=request.data)
    #Validamos si los datos son correctos
    if serializer.is_valid():
        serializer.save() #Guardamos en la Base de Datos
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #Si hay errores devolvemos el error en JSON
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def actualizar_categoria(request, pk):
    #Buscamos la categoría para actualizar
    categoria = get_object_or_404(Categoria, pk=pk)
    #Pasamos el objeto y los datos nuevos al serializer
    serializer = CategoriaSerializer(categoria, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def eliminar_categoria (request, pk):
    #Buscamos la categoría
    categoria = get_object_or_404(Categoria, pk=pk)
    categoria.delete() #Eliminamos
    return Response({"mensaje": "Categoría eliminada"}, status=status.HTTP_204_NO_CONTENT)

@api_view(["POST"])
def crear_producto(request, pk):
    serializer = ProductoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(),
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["PUT"])
def actualizar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    serializer = ProductoSerializer(producto, data=request.data)
    if serializer.is_valid():
        serializer.save(),
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def eliminar_producto(request, pk): 
    categoria = get_object_or_404(Categoria, pk=pk)
    categoria.delete()
    return Response({"mensaje": "Categoría eliminada"}, status=status.HTTP_204_NO_CONTENT)