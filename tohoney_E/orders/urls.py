from django.urls import path
from orders.views import order_complete
urlpatterns = [
    path('order_complete/',order_complete, name="order_complete"),
]
