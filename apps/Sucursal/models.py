from django.db import models

# Create your models here.

class Sucursal (models.Model):
    direccion = models.TextField

    def __str__(self):
        return self.name
