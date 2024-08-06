from rest_framework import serializers

from doob.models import Hospital, Company, Sick, Employee


class NameSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=200, allow_null=False)


class NationalIDSerializer(serializers.Serializer):
    national_id = serializers.ListField(child=serializers.IntegerField(), allow_empty=False)


class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['name', 'manager_name', 'manager_id']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'manager_name', 'manager_id']


class SickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sick
        fields = ['name', 'nationalID', 'illName', 'hospital']


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'nationalID', 'company']
