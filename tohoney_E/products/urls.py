from django.urls import path
from products.views import product,single_product
urlpatterns = [
    path('',product , name='products'),
    path('single_product/',single_product , name='single_products')
]
