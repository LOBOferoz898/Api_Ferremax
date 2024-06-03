from rest_framework import routers
from .api import  ProductViewSet, listar_productos_activos
from rest_framework.routers import DefaultRouter
from django.urls import include, path


router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')



urlpatterns = [
    path('productos/activos/', listar_productos_activos, name='listar_productos_activos'),
    path('', include(router.urls)), #Api CRUD PARA CONTROLAR Y GESTIONAR LOS PRODUCTOS DEL INVENTARIO
]