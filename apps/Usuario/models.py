from django.db import models

# Create your models here.

class Usuario (models.Model):
    nombre_usuario = models.TextField()
    contrasena = models.TextField
    
    def __str__(self):
        return self.name

        

