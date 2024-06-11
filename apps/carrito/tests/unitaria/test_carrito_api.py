import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db 
class TestCarritoApi:
    
    def test_producto_inexistente(self):
        client = APIClient()
        url = reverse('agregar_productos')
        
        data = {
            "product_id": 8,
            "quantity": 3
        }
        
        response = client.post(url,data, format='json')
        
        assert response.status_code == 404
        
        assert response.data["error"] == "El producto no existe"
        
        
        
    def test_type_value_id_agregar_prod(self):
        
        client = APIClient()
        
        url = reverse('agregar_productos')
        data = {
            "product_id": "",
            "quantity": 3
        }
        
        response = client.post(url,data, format='json')
        
        assert response.status_code == 404
        
        assert response.data["error"] == "el id debe ser un valor entero"