from rest_framework import routers
from .api import  PagoViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include, path


router = DefaultRouter()
router.register(r'Pago', PagoViewSet, basename='Pago')

urlpatterns = [
    path('', include(router.urls)), #Api CRUD PARA CONTROLAR Y GESTIONAR LOS PRODUCTOS DEL INVENTARIO
]