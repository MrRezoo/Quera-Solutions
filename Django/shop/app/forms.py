from django import forms
from django.forms import ModelForm

from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'stock']

    def clean_price(self):
        price = self.cleaned_data['price']
        if price > 1000:
            raise forms.ValidationError("Product is too expensive")
        return price

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 20:
            raise forms.ValidationError("Product must have a good description")
        return description
