from django import forms
from .models import Product, Color


class CartForm(forms.Form):
    def __init__(self, *args, **kwargs):
        items = kwargs.pop('items', [])
        super().__init__(*args, **kwargs)

        for item in items:
            self.fields[f'number_{item.id}'] = forms.IntegerField(
                label=item.name,
                initial=1,
                required=False
            )
            self.fields[f'color_{item.id}'] = forms.ChoiceField(
                label='color',
                choices=[(color.id, color.name) for color in item.colors_available.all()],
                required=False
            )

    def clean(self):
        cleaned_data = super().clean()
        for field in self.fields:
            if field.startswith('number_') and not cleaned_data.get(field):
                cleaned_data[field] = 1
            if field.startswith('color_') and not cleaned_data.get(field):
                product_id = field.split('_')[1]
                product = Product.objects.get(id=product_id)
                colors = product.colors_available.all()
                if colors.exists():
                    cleaned_data[field] = colors.order_by('name').first().id
        return cleaned_data
