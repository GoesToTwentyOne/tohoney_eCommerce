from django.contrib import admin
from cart.models import CartModel,CartItemModel

# Register your models here.
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'cart_name', 'cart_created_date', 'cart_last_updated_date']
    prepopulated_fields = {'cart_name': ('cart_id',)}

admin.site.register(CartModel, CartModelAdmin)

class CartItemModelAdmin(admin.ModelAdmin):
    list_display = ['product', 'cart', 'quantity', 'is_active']

admin.site.register(CartItemModel, CartItemModelAdmin)
