from django import forms 
from orders.models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields = [
            'user',
            'payment',
            'order_number',
            'first_name',
            'last_name',
            'company_name',
            'email',
            'phone',
            'country',
            'address_line1',
            'zip',
            'city',
            # 'order_total',
            # 'tax',
            # 'status',
            # 'ip',
            # 'is_ordered',
            # 'created_at',
        ]