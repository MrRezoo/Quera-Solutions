"""Proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from doob.views import get_sick_employee_by_hospital, get_sick_employee_by_company, sms_link
from django.urls import path

urlpatterns = [
    path('get_hospital/', get_sick_employee_by_hospital),
    path('get_company/', get_sick_employee_by_company),
    path('sms/', sms_link),
]
