from datetime import timedelta

from django.db.models import Avg, Count, Sum
from django.utils import timezone

from store.models import Customer, Employee, Order, Product


def young_employees(job: str):
    return Employee.objects.filter(age__lt=30, job=job)


def cheap_products():
    average_price = Product.objects.aggregate(Avg('price'))
    return Product.objects.filter(price__lt=average_price['price__avg']).values_list("name", flat=True).order_by(
        "price")


def products_sold_by_companies():
    return Product.objects.values_list("company__name", Sum("sold"))


def sum_of_income(start_date: str, end_date: str):
    result = Order.objects.filter(time__range=[start_date, end_date]).aggregate(Sum("price"))
    return result["price__sum"]


def good_customers():
    one_month_ago = timezone.now() - timedelta(days=30)
    return (
        Customer.objects.filter(level='G', order__time__gte=one_month_ago)
        .annotate(order_count=Count('order'))
        .filter(order_count__gt=10)
        .values_list('name', 'phone')
    )


def nonprofitable_companies():
    return (
        Product.objects.filter(sold__lt=100)
        .values('company__name')
        .annotate(low_selling_count=Count('id'))
        .filter(low_selling_count__gte=4)
        .values_list('company__name', flat=True)
    )
