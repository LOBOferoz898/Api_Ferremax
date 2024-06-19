# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from .models import Sucursal
from rest_framework import viewsets, permissions
from .serializers import SucursalSerializer



class SucursalViewSet(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SucursalSerializer