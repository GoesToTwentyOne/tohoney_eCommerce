from django.contrib import admin
from products.models import ProductModel

# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['product_name',]}
    list_display=['product_name', 'slug','price','stock_quantity','is_available','category','created_date','last_modified_date' ]
admin.site.register(ProductModel, ProductModelAdmin)