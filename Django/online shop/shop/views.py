import json

from django.http.response import HttpResponse
from django.shortcuts import render
from .forms import *


def cart(request):
    if request.method == 'POST':
        form = CartForm(request.POST, items=Product.objects.all())
        if form.is_valid():
            return HttpResponse(make_json(form))
    else:
        form = CartForm(items=Product.objects.all())
        return render(request, "cart_form.html", {
            'form': form,
        })


def make_json(form):
    products = {}
    orders = []
    data = form.clean()

    for field in form.fields:
        product_id = field.split('_')[1]
        products[product_id] = []

    for field in form.fields:
        product_id = field.split('_')[1]
        products[product_id].append(data[field])

    for product, values in products.items():
        orders.append({"product_id": product, "number": values[0], "color": values[1]})

    return json.dumps(orders)
