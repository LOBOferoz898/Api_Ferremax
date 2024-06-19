from django.db import models

# Create your models here.

class Boleta (models.Model):
    #ID PAGO SALE DE EL COMPONEN PAGO 
    #AGREGAR A LA FUNCION "Pay cart" una funcion que cree el pago y la factura
    id_pago = models.TextField
    # PRODUCTO Y MONTO PAGADO SALE DEL COMPONENTE CARRITO
    productos = models.TextField
    monto_pagado = models.BigIntegerField
    #FECHA DE PAGO SE TOMA LA FECHA DE EL COMPUTADOR
    fecha_pago = models.TextField
    
    def __str__(self):
        return self.name