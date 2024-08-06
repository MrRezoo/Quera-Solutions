from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from doob.models import Company, DeliveryReport, Employee, Hospital, Sick
from doob.serializer import NameSerializer, NationalIDSerializer
from doob.SMS import get_phone_number, sms


@api_view(['POST'])
def get_sick_employee_by_hospital(request):
    serializer = NameSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    hospital_name = serializer.validated_data['name']
    try:
        hospital = Hospital.objects.get(name=hospital_name)
    except Hospital.DoesNotExist:
        return Response({"error": "Hospital not found"}, status=status.HTTP_404_NOT_FOUND)

    sick_employees = Sick.objects.filter(hospital=hospital, illName="Covid19")
    result = {}
    index = 1
    for sick in sick_employees:
        try:
            employee = Employee.objects.get(nationalID=sick.nationalID)
            result[index] = f"({employee.name}, {employee.nationalID})"
            index += 1
        except Employee.DoesNotExist:
            continue
    return Response(result, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_sick_employee_by_company(request):
    serializer = NameSerializer(data=request.data)
    if serializer.is_valid():
        company_name = serializer.validated_data['name']
        company = get_object_or_404(Company, name=company_name)
        employees = Employee.objects.filter(company=company)
        result = {}
        index = 1
        for employee in employees:
            if Sick.objects.filter(nationalID=employee.nationalID, illName="Covid19").exists():
                result[index] = f"({employee.name}, {employee.nationalID})"
                index += 1
        return Response(result, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
async def sms_link(request):
    serializer = NationalIDSerializer(data=request.data)
    if serializer.is_valid():
        national_ids = serializer.validated_data['national_id']
        for national_id in national_ids:
            phone_number = get_phone_number(national_id)
            await sms(phone_number)
            DeliveryReport.objects.create(phone_number=phone_number)
        return Response(status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
