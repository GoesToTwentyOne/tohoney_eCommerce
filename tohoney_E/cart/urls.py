from django.urls import path
from cart.views import cartview,add_to_cart,remove_to_cart,delete_to_cart

urlpatterns = [
    path('',cartview,name='cart'),
    path('add_to_cart/<int:product_id>/',add_to_cart,name='add_to_cart'),
    path('remove_to_cart/<int:product_id>/', remove_to_cart, name='remove_cart'),
    path('delete_to_cart/<int:product_id>/', delete_to_cart, name='delete_cart'),
    
]
