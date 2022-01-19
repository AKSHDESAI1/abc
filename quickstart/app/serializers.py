from django.contrib.auth import models
from rest_framework.utils import field_mapping
from .models import Employee
from rest_framework import serializers
from django.contrib.auth.models import User

# class EmployeeSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=30)
#     email = serializers.EmailField()
#     password = serializers.CharField(max_length=30)
#     phone = serializers.CharField(max_length=10)

#     def create(self, validated_data):
#         print('Create Method Called..', validated_data)
#         return Employee.objects.create(**validated_data)

#     def update(self, employee, validated_data):
#         newEmployee = Employee(**validated_data)
#         newEmployee.id = employee.id
#         newEmployee.save()
#         return newEmployee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class Userserializer(serializers.ModelSerializer):
    # username = serializers.CharField(max_length=30)
    # email = serializers.EmailField()
    # password = serializers.CharField(max_length=30)
    # first_name = serializers.CharField(max_length=30)
    # last_name = serializers.CharField(max_length=30)
    class Meta:
        model = User
        fields = '__all__'
