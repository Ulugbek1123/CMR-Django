from django.forms import ModelForm
from .models import Order

class createOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'