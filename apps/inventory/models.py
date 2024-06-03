from django.db import models

class Product(models.Model):
    nombre = models.TextField()
    description = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=0)
    stock = models.IntegerField()
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name