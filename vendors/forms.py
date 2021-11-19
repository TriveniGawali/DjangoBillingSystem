from django import forms
from vendors.models import Vendors


class Updatevendorforms(forms.ModelForm):
    class Meta:
        model = Vendors
        fields = "__all__"