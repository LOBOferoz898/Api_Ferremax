from django.db import models

# Create your models here.

class Sucursal (models.Model):

    direccion = models.TextField(default="")
    Gerente = models.TextField(default="")
    Cant_Trabajadores = models.TextField(default="")
    
    def __str__(self):
        return self.name
