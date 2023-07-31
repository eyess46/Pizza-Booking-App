from django import forms
from .models import Order
from datetime import datetime





class OrderForm(forms.ModelForm):
    name = forms.CharField(max_length=1000)
    phone_number = forms.CharField(max_length=100)
    date_needed = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    email = forms.EmailField()
    address = forms.CharField(max_length=10000)
    request = forms.CharField(max_length=10000)
    payment_reciept = forms.ImageField()

    class Meta:
        model = Order
        fields =['name', 'phone_number', 'date_needed', 'email', 'address', 'request', 'payment_reciept']
