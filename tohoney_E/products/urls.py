from django.urls import path
from products.views import product,single_product
urlpatterns = [
    path('',product , name='products'),
    path('single_product/',single_product , name='single_products_view'),
    path('category/<slug:category_slug>/',product, name='products_by_category'),
    path('category/<slug:product_slug>/<slug:category_slug>/',single_product, name='single_product'),
]
