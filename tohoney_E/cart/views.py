from django.shortcuts import render,redirect
from products.models import ProductModel
from cart.models import CartModel,CartItemModel

# Create your views here.
def cartview(request):
    session_id=request.session.session_key
    cart_id=CartModel.objects.get(cart_id=session_id)
    total_amount=0
    total_tax=0
    grand_total_amount=0
    cart_items=None
    if cart_id:
        cart_items=CartItemModel.objects.filter(cart=cart_id)
        for item in cart_items:
            total_amount+=(item.product.price * item.quantity) 
        tax=(2*total_amount)/100
        grand_total_amount+=(total_amount+tax)
        
    return render(request,'cart/cart.html',context={'cart_items': cart_items,'total': total_amount, 'grand_total': grand_total_amount,'tax':tax})
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

def remove_to_cart(request,product_id):
    product=ProductModel.objects.get(id=product_id)
    session_id=request.session.session_key
    cart_id=CartModel.objects.get(cart_id=session_id)
    if cart_id:
        cart_item=CartItemModel.objects.get(cart=cart_id,product=product)
        if cart_item.quantity > 1:
            cart_item.quantity -=1
            cart_item.save()
        else:
            cart_item.delete()
    else:
        pass
    return redirect('cart')
def delete_to_cart(request,product_id):
    product=ProductModel.objects.get(id=product_id)
    session_id=request.session.session_key
    cart_id=CartModel.objects.get(cart_id=session_id)
    if cart_id:
        cart_item=CartItemModel.objects.get(cart=cart_id,product=product)
        cart_item.delete()
    else:
        pass
    return redirect('cart')
    
    
def checkout(request):
    return render(request,'cart/checkout.html')

