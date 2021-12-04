from django import forms
from django.forms import fields
from .models import OrderProduct


class InvoiceProductsForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = ('orderno', 'productname', 'qty', 'rate', 'total', 'cgst', 'sgst', 'igst', 'totalamount')
        