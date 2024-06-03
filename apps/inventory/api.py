from .models import Product
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import obtener_productos_activos

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer


@api_view(['GET'])
def listar_productos_activos(request):
    """
    API para obtener todos los productos activos.
    """
    productos = obtener_productos_activos()
    serializer = ProductSerializer(productos, many=True)
    return Response(serializer.data)
