from rest_framework import serializers

from .models import Classroom


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = "__all__"

    @staticmethod
    def validate_capacity(val):
        if val < 5:
            raise serializers.ValidationError("Capacity should be equal or more than 5")
        return val

    @staticmethod
    def validate_area(val):
        if val < 0:
            raise serializers.ValidationError("Area should be positive")
        return val
