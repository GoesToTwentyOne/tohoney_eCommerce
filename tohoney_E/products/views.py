from django.shortcuts import render,get_object_or_404
from products.models import ProductModel
from category.models import CategoryModel

# Create your views here.
def product(request,category_slug=None):
    categories=CategoryModel.objects.all()
    if category_slug is not None:
        category=get_object_or_404(CategoryModel,slug=category_slug)
        products=ProductModel.objects.filter(is_available=True,category=category)
    else:
        category=None
        products=ProductModel.objects.filter(is_available=True)
    return render(request,'products/shop.html',context={'products':products,'categories':categories})

def single_product(request):
    return render(request,'products/single-product.html')
