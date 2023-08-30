from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from accounts.forms import RegistrationForm
from .models import Account
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            print(last_name)
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            print(email)
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            user.phone_number = phone_number
            user.save()
    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)



def user_login(request):
    form=RegistrationForm()
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        login(request, user)
        return redirect('dashboard')

    return render(request, 'accounts/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')  
    
def user_wishlist(request):
    return render(request, 'accounts/wishlist.html')
def user_dashboard(request):
    return render(request, 'accounts/dashboard.html')