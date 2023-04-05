from django.db.models import Sum, IntegerField, Count, Q
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
    q = Rider.objects.filter(riderequest__ride__car__car_type="A").annotate(
        n=Count(
            "riderequest__ride",
            filter=Q(riderequest__ride__car__car_type='A')
        )
    )
    return q


def query_8(x):
    q = Driver.objects.filter(car__model__gte=x).values('account__email').distinct()
    return q


def query_9():
    q = Driver.objects.annotate(n=Count("car__ride"))
    return q


def query_10():
    q = Driver.objects.filter(account__drivers__isnull=False).values('account__first_name').annotate(
        n=Count('account__drivers__car__ride')
    )
    return q


def query_11(n, c):
    q = Driver.objects.filter(car__color=c, car__model__gte=n).distinct()
    return q


def query_12(n, c):
    car_with_color_c = Car.objects.filter(color=c).values('driver')
    car_with_model_n_or_above = Car.objects.filter(model__gte=n).values('driver')
    q = Driver.objects.filter(car__in=car_with_color_c).filter(car__in=car_with_model_n_or_above).distinct()
    return q


def query_13(n, m):
    q = Ride.objects.filter(car__owner__account__first_name=n,
                            request__rider__account__first_name=m).aggregate(
        sum_duration=Sum('dropoff_time') - Sum('pickup_time'))

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
