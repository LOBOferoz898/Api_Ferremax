# cart/services.py

from decimal import Decimal
from .models import CartItem, Order, OrderItem
from apps.inventory.models import Product

def add_product_to_cart(product_id, quantity):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return {"error": "El producto no existe"}, 404
    except:
        return {"error": "el id debe ser un valor entero"}, 404
    
    try: 
        product = Product.objects.get(quantity=quantity)
    except:
        pass
    
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += int(quantity)
    else:
        cart_item.quantity = int(quantity)
    cart_item.save()

    return {"product": product, "quantity": cart_item.quantity}, 200

def pay_cart():
    cart_items = CartItem.objects.all()
    if not cart_items.exists():
        return {"error": "Cart is empty"}, 400

    total_price = sum(item.product.precio * item.quantity for item in cart_items)
    order = Order.objects.create(total_price=total_price)

    for item in cart_items:
        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
        item.delete()  # Remove item from cart after it has been added to the order

    return {"order_id": order.id, "total_price": total_price}, 200
