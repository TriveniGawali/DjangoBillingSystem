from django import forms
from products.models import Products


class Updateproductforms(forms.ModelForm):
    class Meta:
        model = Products
        fields = "__all__"