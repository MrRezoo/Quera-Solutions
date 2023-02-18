from django.db.models import F, Sum
from django.shortcuts import get_object_or_404

from app.models import Order


def checkout(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    order_items = order.orderitem_set.select_related('product')
    # total_price = order_items.aggregate(
    #     total_price=Sum(F('product__price') * F('quantity'))
    # )
    total_price = sum(
       [item.product.price * item.quantity for item in order_items]
    )
    return {'total_price': f'{total_price["total_price"]:.2f}'}

