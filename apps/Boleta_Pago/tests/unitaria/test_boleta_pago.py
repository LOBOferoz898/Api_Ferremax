import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db 
class TestBoletaPagoApi:
    
    def test_producto_inexistente(self):
        client = APIClient()
        url = reverse('')
        
        data = {

        }
        
        response = client.post(url,data, format='json')
        
        assert response.status_code == 404
        
        assert response.data["error"] == "El producto no existe"
        