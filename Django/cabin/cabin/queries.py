from django.db.models import Sum, IntegerField, Count
from django.db.models.functions import Coalesce

from .models import *


def query_0():
    q = Driver.objects.all()
    return q


def query_1():
    """
    :return: {'income': value }
    """
    q = Payment.objects.aggregate(
        income=Coalesce(Sum('amount', output_field=IntegerField()), 0)
    )

    return q


def query_2(x):
    """
    :param x: ID of Rider
    :return {'payment_sum': value}:  Sum of all payments made by rider with id x
    """
    q = (
        Payment.objects.filter(ride__request__rider=x).aggregate(
            payment_sum=Coalesce(Sum('amount', output_field=IntegerField()), 0)
        )
    )

    return q


def query_3():
    """
    :return: Number of driver who have more than 1 car class A
    """
    q = Driver.objects.filter(car__car_type='A').distinct().count()
    return q


def query_4():
    q = RideRequest.objects.filter(ride=None)
    return q


def query_5(t):
    q = Rider.objects.annotate(
        total_paymeny=Sum("riderequest__ride__payment__amount")
    ).filter(total_paymeny__gte=t)

    return q


def query_6():
    q = Account.objects.filter(drivers__isnull=False).annotate(
        num_cars=Count('drivers__car')).order_by('-num_cars', 'last_name').first()
    return q


def query_7():
    """

    :return: A list of all passengers who had at least one trip in a class A car, with an additional column
    named n indicating the number of trips each passenger has had in a class A car.
    """
    q = Rider.objects.filter(riderequest__car_type="A").annotate(n=Count("riderequest__ride"))
    return q


def query_8(x):
    q = 'your query here'
    return q


def query_9():
    q = 'your query here'
    return q


def query_10():
    q = 'your query here'
    return q


def query_11(n, c):
    q = 'your query here'
    return q


def query_12(n, c):
    q = 'your query here'
    return q


def query_13(n, m):
    q = 'your query here'
    return q


def query_14(x, y, r):
    q = 'your query here'
    return q


def query_15(n, c):
    q = 'your query here'
    return q


def query_16(x, t):
    q = 'your query here'
    return q


def query_17():
    q = 'your query here'
    return q


def query_18():
    q = 'your query here'
    return q


def query_19(n, t):
    q = 'your query here'
    return q


def query_20():
    q = 'your query here'
    return q
