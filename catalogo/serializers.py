from rest_framework import serializers
from .models import Categoria, Producto, Marca

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre', 'descripcion']

class ProductoSerializer(serializers.ModelSerializer):

    categoria = serializers.StringRelatedField()

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'marca', 'categoria']

class MarcaSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True, read_only=True)

    class Meta:
        model = Marca
        fields = ['id', 'nombre', 'pais', 'descripcion', 'productos']