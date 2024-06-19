from django.db import models

# Create your models here.

class Categoria (models.Model):
    id_categoria = models.TextField
    Nombre = models.TextField
    desc_categoria = models.TextField

    def __str__(self):
        return self.name
