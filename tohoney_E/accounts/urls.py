from django.urls import path
from accounts.views import user_register,user_login,user_wishlist
urlpatterns = [
    path('register/',user_register,name="register"),
    path('login/',user_login,name="login"),
    path('wish/',user_wishlist,name="wishlist"),
]
