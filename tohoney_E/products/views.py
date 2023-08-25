from django.shortcuts import render

# Create your views here.
def product(request):
    return render(request,'products/shop.html')

def single_product(request):
    return render(request,'products/single-product.html')
