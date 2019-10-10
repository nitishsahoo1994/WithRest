from restapp.models import Employee
from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    eno = serializers.IntegerField()
    ename = serializers.CharField(max_length=64)
    esal = serializers.FloatField()
    eaddr = serializers.CharField(max_length=264)
    def create(self, validated_data):
        return Employee.objects.create(**validated_data)
