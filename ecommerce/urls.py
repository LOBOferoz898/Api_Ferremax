from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Inventario/', include('apps.inventory.urls')),
    path('Carrito/', include('apps.carrito.urls')),
    path('Pago/', include('apps.Pago.urls')),
    path('Usuarios/', include('apps.Usuario.urls')),
    path('Sucursales/', include('apps.Sucursal.urls')),
    
    
]