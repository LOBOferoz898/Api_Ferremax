from .models import Product

def obtener_productos_activos():
    """
    Retorna una lista de todos los productos activos.
    """
    return Product.objects.filter(activo=True)