from re import I
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators import csrf
from .models import Employee
from .serializers import EmployeeSerializer, Userserializer
from django.contrib.auth.models import User
# from app import serializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.
from rest_framework import status


@csrf_exempt
def employeeListView(request):
    if request.method == 'GET':

        employees = Employee.objects.all()
        # return JsonResponse("Hello There...", False)
        # return JsonResponse({"message":"Success"})
        serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        jsonData = JSONParser().parse(request)
        serializer = EmployeeSerializer(data=jsonData)
        print(jsonData)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)


def UserListView(request):
    user = User.objects.all()
    serializer = Userserializer(user, many=True)
    print(user)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def employeeDetailView(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
        print(employee)

    except Employee.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'DELETE':
        employee.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return JsonResponse(serializer.data, safe=False)
        # return JsonResponse("Employee" + str(pk), safe=False)
    elif request.method == 'PUT':
        jsonData = JSONParser().parse(request)
        serializer = EmployeeSerializer(employee, data=jsonData)
        print(jsonData)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse(serializer.errors, safe=False)
