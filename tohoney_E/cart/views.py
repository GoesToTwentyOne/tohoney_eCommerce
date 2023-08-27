from django.shortcuts import render,redirect
from products.models import ProductModel
from cart.models import CartModel,CartItemModel

# Create your views here.
def cartview(request):
    return render(request,'cart/cart.html')
def add_to_cart(request,product_id):
    product=ProductModel.objects.get(id=product_id)
    session_id=request.session.session_key
    cart_id=CartModel.objects.filter(cart_id=session_id).exists()
    if cart_id :
        cart_item=CartItemModel.objects.filter(product=product_id).exists()
        if cart_item:
            item=CartItemModel.objects.get(product=product)
            item.quantity+=1
            item.save()
        else:
            cart_id=CartModel.objects.get(cart_id=session_id)
            item=CartItemModel.objects.create(
                cart=cart_id,
                product=product,
                quantity=1
            )
    else:
        cart=CartModel.objects.create(cart_id=session_id)
        cart.save()
    return redirect('cart')
    
def checkout(request):
    return render(request,'cart/checkout.html')

