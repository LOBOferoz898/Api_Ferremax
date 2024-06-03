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



``
# Utilizacion de las diferentes funciones de las  APIS

#Para consultar productos activos de la lista de productos existentes.

Ruta = http://127.0.0.1:8000/api/productos/activos
Metodo = Get
Parametros = N/A
Headers = N/A
Body = N/A

#Para Agregar un nuevo producto al CARRITO.

Ruta = http://127.0.0.1:8000/api/carro/agregar/
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

#Para ver el carrito 

Ruta = http://127.0.0.1:8000/api/cart-items
Metodo = Get
Parametros = N/A
Headers = N/A
Body = N/A

#En el caso de que el carrito tenga objetos agregados desplegara la misma informacion que el item anterior y en el caso de que no exista objetos en el carrito indicara que el carrito esta vacio.

#Para pagar el carrito actual

Ruta = http://127.0.0.1:8000/api/carro/pagar/
Metodo = Post
Parametros = N/A
Headers = N/A
Body = N/A

#En el caso de que la "Compra" haya sido exitosa indicara un mensaje con la orden de compra y el precio pagado:
{
    "order_id": 4,
    "total_price": 42000.0
}

#Para ver los productos existentes y que se pueden comprar:

Ruta = http://127.0.0.1:8000/api/products
Metodo = Get
Parametros = N/A
Headers = N/A
Body = N/A
#Si todo esta correcto desplegara una lista con los datos de los productos existentes 

#Para agregar un producto a la lista de productos 

Ruta = http://127.0.0.1:8000/api/products/
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

#Para actualizar un producto de la lista de productos tendras que agregar la id a la ruta sustituyendo "Id_del_producto" por la id a actualizar

Ruta = http://127.0.0.1:8000/api/products/id_del_producto/
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

#Para elimitar algun producto existentes de la lista se sustituira el "id_del_producto" por la id de el producto que se desee eliminar:

Ruta = http://127.0.0.1:8000/api/products/id_del_producto/
Metodo = DELETE
Parametros = N/A
Headers = N/A
Body = N/A

#En el caso que la id ingresada no exista dira el siguiente mensaje: 

{
    "detail": "No Product matches the given query."
}