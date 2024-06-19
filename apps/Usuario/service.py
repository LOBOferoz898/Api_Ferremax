from .models import Usuario
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.contrib.auth.hashers import make_password

def add_user(nombre,contrasena):
    try:
        existing_user = Usuario.objects.get(nombre_usuario=nombre)
        return {"error": "El nombre de usuario ya existe"}, 400
    except ObjectDoesNotExist:
        pass
    except ValidationError:
        return {"error": "Nombre de usuario no válido"}, 400
    try:
        
        hashed_password = make_password(contrasena)  
        new_user = Usuario(nombre_usuario=nombre, contrasena=hashed_password)
        new_user.save()
        return {"message": "Usuario creado con éxito!"}, 200
    except ValidationError:
        return {"error": "Datos no válidos o vacíos"}, 400
    except Exception as e:
        return {"error": f"Error al crear el usuario: {e}"}, 500
    
    

