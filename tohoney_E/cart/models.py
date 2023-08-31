from django.db import models
from products.models import ProductModel
from accounts.models import Account

# Create your models here.
class CartModel(models.Model):
    cart_id=models.CharField(max_length=255,blank=True,null=True)
    cart_name=models.CharField(max_length=255, blank=True,null=True)
    cart_created_date=models.DateField(auto_now_add=True)
    cart_last_updated_date=models.DateField(auto_now=True)
    
    # def __str__(self):
    #     return self.cart_id

class CartItemModel(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    product=models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    cart=models.ForeignKey(CartModel, on_delete=models.CASCADE,null=True)
    quantity=models.IntegerField()
    is_active=models.BooleanField(default=True)
    
    def sub_total(self):
        return self.product.price * self.quantity
    def __str__(self):
        return self.product.product_name