from re import I
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators import csrf
from .models import Employee
from .serializers import EmployeeSerializer, Userserializer
from django.contrib.auth.models import User
# from app import serializers
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# @csrf_exempt


@api_view(['GET', 'POST'])
def employeeListView(request):
    if request.method == 'GET':

        employees = Employee.objects.all()
        # return JsonResponse("Hello There...", False)
        # return JsonResponse({"message":"Success"})
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)
        # return Response(serializer.data, safe=False)
    elif request.method == 'POST':
        # jsonData = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=request.data)
        # print(jsonData)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['DELETE', 'GET', 'PUT'])
def employeeDetailView(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        print(employee)

    except Employee.DoesNotExist:
        return Response(status=404)

    if request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
        # return JsonResponse("Employee" + str(pk), safe=False)
    elif request.method == 'PUT':
        # jsonData = JSONParser().parse(request)
        serializer = EmployeeSerializer(employee, data=request.data)
        # print(jsonData)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET'])
def UserListView(request):
    if request.method == 'GET':
        user = User.objects.all()
        serializer = Userserializer(user, many=True)
        print(user)
        return Response(serializer.data)
