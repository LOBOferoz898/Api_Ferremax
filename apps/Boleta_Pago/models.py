from django.db import models

# Create your models here.

class Boleta (models.Model):

    id_pago = models.TextField
    productos = models.TextField
    monto_pagado = models.BigIntegerField
    
    def __str__(self):
        return self.name