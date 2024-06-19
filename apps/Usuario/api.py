from rest_framework.decorators import api_view
from rest_framework.response import Response
from .service import  add_user


@api_view(['POST'])
def new_user(request):
    user = request.data.get('nombre_usuario')
    password = request.data.get('contrasena')

    result, status_code = add_user(user, password)
    if status_code == 404:
        return Response(result, status=status_code)
    
    return Response(result, status=status_code)


