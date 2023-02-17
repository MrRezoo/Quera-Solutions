from django.db.models import Sum
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from app.models import Order


def checkout(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    price = order.orderitem_set.aggregate(total_price=Sum('product__price'))
    price['total_price'] = str(price['total_price'])
    return JsonResponse(price)
