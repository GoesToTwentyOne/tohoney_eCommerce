from django.urls import path
from accounts.views import user_register,user_login,user_wishlist,user_dashboard,user_logout
urlpatterns = [
    path('register/',user_register,name="register"),
    path('login/',user_login,name="login"),
    path('logout/',user_logout,name="logout"),
    path('wish/',user_wishlist,name="wishlist"),
    path('dashboard/',user_dashboard,name="dashboard"),
]
