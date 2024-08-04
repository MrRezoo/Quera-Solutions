from django import forms


class CartForm(forms.Form):
    def __init__(self, *args, **kwargs):
        items = kwargs.pop('items', [])
        super(CartForm, self).__init__(*args, **kwargs)
        for item in items:
            self.fields['number_%s' % item.id] = forms.IntegerField(
                label=item.name,
                initial=1,
                required=False
            )
            self.fields['color_%s' % item.id] = forms.ChoiceField(
                label='color',
                choices=[(color.id, color.name) for color in item.colors_available.all()],
                required=False
            )

    def is_valid(self):
        valid = super(CartForm, self).is_valid()
        if not valid:
            return valid

        for field_name, field in self.fields.items():
            if field_name.startswith('number_') and not self.cleaned_data.get(field_name):
                self.cleaned_data[field_name] = 1
            elif field_name.startswith('color_') and not self.cleaned_data.get(field_name):
                product_id = field_name.split('_')[1]
                product = next(item for item in self.items if str(item.id) == product_id)
                self.cleaned_data[field_name] = min(product.colors_available.all(), key=lambda color: color.name).id

        return True
