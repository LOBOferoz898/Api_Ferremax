from django.db import models

# Create your models here.

class Pago (models.Model):
    id_pago = models.TextField
    monto_pagar = models.BigIntegerField
    usuario = models.TextField
    Metodo_Pago = models.TextField

    def __str__(self):
        return self.name
