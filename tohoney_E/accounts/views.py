from django.shortcuts import render

# Create your views here.
def user_register(request):
    return render(request, 'accounts/register.html')
def user_login(request):
    return render(request, 'accounts/login.html')
def user_wishlist(request):
    return render(request, 'accounts/wishlist.html')
def user_dashboard(request):
    return render(request, 'accounts/dashboard.html')