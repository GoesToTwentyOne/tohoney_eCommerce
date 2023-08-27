from django.urls import path
from cart.views import cartview,checkout,add_to_cart

urlpatterns = [
    path('',cartview,name='cart'),
    path('<int:product_id>/',add_to_cart,name='add_to_cart'),
    path('checkout/',checkout,name='checkout')
]
