from rest_framework import routers
from .views import  UsuarioViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .api import new_user


router = DefaultRouter()
router.register(r'', UsuarioViewSet, basename='Usuario')



urlpatterns = [
    path('Agregar_usuario/', new_user , name='agregar_usuario'),
    path('', include(router.urls)), #Api CRUD PARA CONTROLAR Y GESTIONAR LOS USUARIOS
]
    