from django.shortcuts import render
from cart.models import CartModel,CartItemModel

# Create your views here.
def get_session_create(request):
    if not request.session.session_key:
        request.session.create()
        return request.session.session_key
def order_complete(request):
    return render(request, 'orders/order_complete.html')


def place_order(request):
    print(request.POST)
    cart_items=None
    total_amount=0
    tax_amount=0
    grand_total_amount=0
    cart_items=CartItemModel.objects.filter(user=request.user)
    for item in cart_items:
        total_amount += (item.product.price*item.quantity)
    tax_amount=(2*total_amount)/100
    grand_total_amount += (total_amount+tax_amount)
    return render(request,'orders/checkout.html',context={'cart_items': cart_items,'total': total_amount, 'grand_total': grand_total_amount,'tax':tax_amount})

