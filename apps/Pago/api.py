from .models import Pago
from rest_framework import viewsets, permissions
from .serializers import PagoSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PagoSerializer
