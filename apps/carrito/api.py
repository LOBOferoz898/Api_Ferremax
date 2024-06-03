# cart/api.py

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import add_product_to_cart, pay_cart
from .models import CartItem
from .serializers import CartItemSerializer, OrderSerializer

@api_view(['POST'])
def add_to_cart(request):
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)

    result, status_code = add_product_to_cart(product_id, quantity)
    if status_code == 404:
        return Response(result, status=status_code)

    cart_item = CartItem.objects.get(product_id=product_id)
    serializer = CartItemSerializer(cart_item)
    return Response(serializer.data)

@api_view(['POST'])
def pay_for_cart(request):
    result, status_code = pay_cart()
    return Response(result, status=status_code)
