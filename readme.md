### 1. Configuración del Entorno
```bash
# Creación del entorno virtual y activación
pip install virtualenv
virtualenv env
# El siguiente comando es solo para windows
.\env\Scripts\activate

# Instalación de dependencias iniciales

# Instalación de Django

pip install Django

# Instalación de las dependencias
pip install -r requirements.txt


# Instalación de Django RestFramework

pip install Djangorestframework




# UTILIZACION DE LAS DIFERENTES FUNCIONES DE LAS APIS:



*********************  API INVENTARIO  *********************

************************************************************************
#Para consultar productos activos de la lista de productos existentes.
************************************************************************
RUTA = http://127.0.0.1:8000/Inventario/productos/activos/
METODO = GET
PARAMETROS = N/A
HEADERS = N/A
BODY = N/A
------------------------------------------------------------------------
------------------------------------------------------------------------

************************************************************************
#Para ver los productos existentes y que se pueden comprar:
************************************************************************

Ruta = http://127.0.0.1:8000/Inventario/productos/
Metodo = Get
Parametros = N/A
Headers = N/A
Body = N/A
#Si todo esta correcto desplegara una lista con los datos de los productos existentes 

------------------------------------------------------------------------
------------------------------------------------------------------------

************************************************************************
#Para agregar un producto a la lista de productos 
************************************************************************

Ruta = http://127.0.0.1:8000/Inventario/productos/
Metodo = Post
Parametros = N/A
Headers = N/A
Body (Raw - Json ) = 
{
    "nombre" : "Nombre del producto",
    "description" : "Descripcion del producto",
    "precio" : Precio del producto,
    "stock" : Stock del producto,
    "activo": Si esta activo o no (False o True)
} 
#En el caso de que todos los datos esten bien se desplegara la informacion del producto creado.

#En el caso de que el dato ingresado sea invalido de desplegara un aviso, por ejemplo si ingresa una letra en el precio se desplegara el siguiente mensaje:
{
    "precio": [
        "A valid number is required."
    ]
}
------------------------------------------------------------------------
------------------------------------------------------------------------

************************************************************************
#Para actualizar un producto de la lista de productos tendras que agregar la id a la ruta sustituyendo "Id_del_producto" por la id a actualizar
************************************************************************

Ruta = http://127.0.0.1:8000/Inventario/productos/id_del_producto/
Metodo = Patch
Parametros = N/A
Headers = N/A
Body (Raw - Json ) = 
 {
    "nombre": "Nuevo nombre del producto",
    "description": "Nueva descripcion",
    "precio": Nuevo Precio,
    "stock": Nuevo Stock
}

#Como el item anterior si los datos son validos mostrara los nuevos datos del producto y si no mostrara un mensaje de error de datos invalidos

------------------------------------------------------------------------
------------------------------------------------------------------------

************************************************************************
#Para elimitar algun producto existentes de la lista se sustituira el "id_del_producto" por la id de el producto que se desee eliminar:
************************************************************************
Ruta = http://127.0.0.1:8000/Inventario/productos/id_del_producto/
Metodo = DELETE
Parametros = N/A
Headers = N/A
Body = N/A

#En el caso que la id ingresada no exista dira el siguiente mensaje: 

{
    "detail": "No Product matches the given query."
}

------------------------------------------------------------------------
------------------------------------------------------------------------



*********************  API CARRITO  *********************

************************************************************************
#Para Agregar un nuevo producto al CARRITO.
************************************************************************
Ruta = http://127.0.0.1:8000/Carrito/agregar/
Metodo = Post
Parametros = N/A
Headers = N/A

# Donde X sera el numero de la id de el producto que desea agregar el carrito e Y sera la cantidad que desea agregar
Body (Raw - Json) = 
{
  "product_id": X,
  "quantity": Y
}

#En el caso de que el producto ingresado en X no exista se desplegara el siguiente mensaje:
{
    "error": "Product not found"
}

#En el caso de que los datos ingresados sean validos se mostraran por consola los datos del producto agregado al carrito como por ejemplo (En este caso se uso la id 5):
{
    "id": 5,
    "product": {
        "id": 5,
        "nombre": "martillo",
        "description": "con mango ajustable a la mano para mejorar la comodidad",
        "precio": "14000",
        "stock": 10,
        "activo": true,
        "created_at": "2024-05-22T15:36:40.236916Z"
    },
    "quantity": 3

------------------------------------------------------------------------
------------------------------------------------------------------------

************************************************************************
#Para ver el carrito 
************************************************************************
Ruta = http://127.0.0.1:8000/Carrito/cart-items/
Metodo = Get
Parametros = N/A
Headers = N/A
Body = N/A

#En el caso de que el carrito tenga objetos agregados desplegara la misma informacion que el item anterior y en el caso de que no exista objetos en el carrito indicara que el carrito esta vacio.

------------------------------------------------------------------------
------------------------------------------------------------------------

************************************************************************
#Para pagar el carrito actual
************************************************************************

Ruta = http://127.0.0.1:8000/Carrito/pagar/
Metodo = Post
Parametros = N/A
Headers = N/A
Body = N/A

#En el caso de que la "Compra" haya sido exitosa indicara un mensaje con la orden de compra y el precio pagado:
{
    "order_id": 4,
    "total_price": 42000.0
}

------------------------------------------------------------------------
------------------------------------------------------------------------



*********************  API USUARIO  *********************

************************************************************************
#Api para listar todos los usuarios registrados
************************************************************************
Ruta = http://127.0.0.1:8000/Usuarios/
Metodo = GET
Parametros = N/A
Headers = N/A
Body = N/A


------------------------------------------------------------------------
------------------------------------------------------------------------

************************************************************************
#Api para agregar un usuario
************************************************************************
Ruta = http://127.0.0.1:8000/Usuarios/Agregar_usuario/
Metodo = POST
Parametros = N/A
Headers = N/A

Body (Raw - Json) = 
{
    "nombre_usuario": "usuario",
    "contrasena": "contrasena"
}

#En el caso de que el usuario ingresado exista se desplegara el siguiente mensaje:

{
    "error": "El nombre de usuario ya existe"
}

#En el caso de que los datos ingresados sean validos se mostraran por consola el siguiente mensaje:

{
    "message": "Usuario creado con éxito!"
}

------------------------------------------------------------------------
------------------------------------------------------------------------



*********************  API SUCURSAL  *********************

************************************************************************
##listar sucursales
************************************************************************
Ruta = http://127.0.0.1:8000/Sucursales/
Metodo = GET
Parametros = N/A
Headers = N/A
Body = N/A

------------------------------------------------------------------------
------------------------------------------------------------------------

************************************************************************
##agregar sucursal
************************************************************************
Ruta = http://127.0.0.1:8000/Sucursales/Agregar_local/
Metodo = Post
Parametros = N/A
Headers = N/A
Body = 
{
    "direccion": "direccion",
    "Gerente": "gerente",
    "Cant_Trabajadores": numero
}

#En caso de problemas al momento de ingresar los datos tendremos posiblemente algunos de estos errores:

{
    "error": "Datos ingresados invalidos o vacios"
}


{
    "error": "La direccion ya posee un local existente"
}

{
    "error": "Direccion no valida"
}
#En el caso de que los datos ingresados sean validos se mostraran por consola el siguiente mensaje:

{
    "message": "Sucursal Registrado!"
}



------------------------------------------------------------------------
------------------------------------------------------------------------

*********************  API PAGO  *********************

************************************************************************

************************************************************************
Ruta = http://127.0.0.1:8000/Carrito/pagar/
Metodo = Post
Parametros = N/A
Headers = N/A
Body = N/A

------------------------------------------------------------------------
------------------------------------------------------------------------

*********************  API BOLETA PAGO  *********************

************************************************************************

************************************************************************
Ruta = http://127.0.0.1:8000/Carrito/pagar/
Metodo = Post
Parametros = N/A
Headers = N/A
Body = N/A

------------------------------------------------------------------------
------------------------------------------------------------------------