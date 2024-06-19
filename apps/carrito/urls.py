from django.urls import include, path
from .api import add_to_cart, pay_for_cart
from rest_framework.routers import DefaultRouter
from .views import CartItemViewSet

router = DefaultRouter()
router.register(r'cart-items', CartItemViewSet)

urlpatterns = [
    path('agregar/', add_to_cart, name='agregar_productos'),
    path('pagar/',  pay_for_cart, name='pagar_carro'),
    path('',include(router.urls), name="CartItemViewSet"),
]