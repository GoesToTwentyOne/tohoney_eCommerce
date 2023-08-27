from django.db import models
from category.models import CategoryModel


# Create your models here.
class ProductModel(models.Model):
    product_name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(max_length=150,unique=True)
    description=models.TextField(max_length=255,blank=True)
    price=models.DecimalField(max_digits=12,decimal_places=2)
    product_image=models.ImageField(max_length=150,upload_to='images/product')
    stock_quantity=models.IntegerField()
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    last_modified_date=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product_name