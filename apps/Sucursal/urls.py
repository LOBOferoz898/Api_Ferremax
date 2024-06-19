from rest_framework import routers
from .views import  SucursalViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .api import new_local


router = DefaultRouter()
router.register(r'', SucursalViewSet, basename='Sucursal')



urlpatterns = [
    path('Agregar_local/', new_local , name='agregar_local'),
    path('', include(router.urls)), #Api CRUD PARA CONTROLAR Y GESTIONAR LAS SUCURSALES
]