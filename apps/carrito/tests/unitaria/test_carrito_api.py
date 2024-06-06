import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status

@pytest.mark.django_db 
class TestCarritoApi:
    def test_agregar_productos(self):
        client = APIClient()
        url = reverse('agregar_productos')
        
        data = {
            "product_id": 6,
            "quantity": 3
        }
        
        response = client.post(url,data, format='json')
        
        
        
        