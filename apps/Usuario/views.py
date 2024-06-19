# Create your views here.
from django.shortcuts import render
from .models import Usuario
from rest_framework import viewsets, permissions
from .serializers import UsuarioSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UsuarioSerializer
