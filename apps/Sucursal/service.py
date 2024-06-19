from .models import Sucursal
from django.core.exceptions import ObjectDoesNotExist, ValidationError




def add_local(direccion, Gerente, Cant_Trabajadores):
    if not direccion or not Gerente or not Cant_Trabajadores:
        return {"error": "Datos ingresados invalidos o vacios"}, 400

    try:
        existing_local = Sucursal.objects.get(direccion=direccion)
        return {"error": "La direccion ya posee un local existente"}, 400
    except ObjectDoesNotExist:
        pass
    except ValidationError:
        return {"error": "Direccion no valida"}, 400

    try:
        new_local = Sucursal(direccion=direccion, Gerente=Gerente, Cant_Trabajadores=Cant_Trabajadores)
        new_local.save()
        return {"message": "Sucursal Registrado!"}, 200
    except ValidationError:
        return {"error": "Datos no válidos o vacíos"}, 400
    except Exception as e:
        return {"error": f"Error al registrar sucursal: {e}"}, 500 