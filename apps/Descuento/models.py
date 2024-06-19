from django.db import models

# Create your models here.
class Descuento (models.Model):
    
    fecha_inicio = models.TextField
    fecha_fin = models.TextField
    nombre = models.TextField
    activo = models.BooleanField(default = False)
    monto_descuento = models.BigIntegerField

    def __str__(self):
        return self.name

