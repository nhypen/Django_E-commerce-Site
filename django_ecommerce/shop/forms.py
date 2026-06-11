from django import forms
from .models import Order


class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        initial=1,
        label="Ilość"
    )


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["full_name", "email", "address"]
        labels = {
            "full_name": "Imię i nazwisko",
            "email": "Email",
            "address": "Adres dostawy",
        }