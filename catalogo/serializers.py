from rest_framework import serializers
from .models import categoria, producto, marca

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = categoria
        fields = ['id', 'nombre', 'descripcion']

class ProductoSerializer(serializers.ModelSerializer):

    categoria = serializers.StringRelatedField()

    class Meta:
        model = producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'marca', 'categoria']

class MarcaSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True, read_only=True)

    class Meta:
        model = marca
        fields = ['id', 'nombre', 'pais', 'descripcion', 'productos']