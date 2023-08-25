from django.urls import path
from cart.views import cart,checkout

urlpatterns = [
    path('',cart,name='cart'),
    path('checkout/',checkout,name='checkout')
]
