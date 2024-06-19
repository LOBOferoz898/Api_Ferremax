from rest_framework.decorators import api_view
from rest_framework.response import Response
from .service import  add_local


@api_view(['POST'])
def new_local(request):
    direccion = request.data.get('direccion')
    gerente = request.data.get('Gerente')
    Cant_Trabajadores = request.data.get('Cant_trabajadores')

    result, status_code = add_local(direccion,gerente,Cant_Trabajadores)
    if status_code == 404:
        return Response(result, status=status_code)
    
    return Response(result, status=status_code)