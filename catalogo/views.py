from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import Categoria, Producto, Marca
from .serializers import CategoriaSerializer, ProductoSerializer, MarcaSerializer


# ---------------------------------
# Rregistro de usuario
# ---------------------------------

@api_view(['POST'])
@permission_classes([AllowAny])
def registro(request):
    """
    Crea un nuevo usuario.
    Datos esperados en el body (JSON)
    {
        "username": "ejemplo"
        "password": "1234",
    }
    """

    username = request.data.get('username')
    password = request.data.get('password')

    #Validación básica
    if not username or not password:
        return Response({"error": "Username y password son requeridos"}, status=400)

    #Crear usuario
    user = User.objects.create_user(username=username, password=password) 
    token, created = Token.objects.get_or_create(user=user)

    return Response({"token": token.key}, status=201)


# ---------------------------------
# Login de usuario
# ---------------------------------

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """
    Autentica al usuario y devuelve un token
    Datos esperados:
    {
        "username": "ejemplo",
        "password": "1234"
    }
    """
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user: 
        token, created = Token.objects.get_or_create(user=user)
        return Response([{"token": token.key}, {"mensaje": "Iniciaste sesión correctamente"}], status=200)
    else:
        return Response({"error": "Credenciales inválidas"}, status=400)
    

# ---------------------------------
# Logout
# ---------------------------------
@api_view(['POST'])
def logout(request):
    """
    Elimina el token del usuario actual (cerrar sesión)
    """
    request.user.auth_token.delete()
    return Response({"mensaje": "Sesión cerrada correctamente"}, status=200)


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
