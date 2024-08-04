import json

from django import forms


class CartForm(forms.Form):
    def __init__(self, *args, **kwargs):
        items = kwargs.pop('items')
        super(CartForm, self).__init__(*args, **kwargs)
        for item in items:
            self.fields['number_%s' % item.id] = forms.IntegerField(label=item.name)
            self.fields['color_%s' % item.id] = forms.ModelChoiceField(label='color',
                                                                       queryset=item.colors_available.all())