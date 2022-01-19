from django.shortcuts import render, resolve_url
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course, CourseSerializer
from rest_framework import status
from django.http import Http404
from rest_framework import mixins, generics
# Create your views here.


class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# class CourseDetailView(generics.RetrieveDestroyAPIView):
    # queryset = Course.objects.all()
    # serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# class CourseDetailView(generics.RetrieveUpdateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer




# class CourseListView(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

# class CourseDetailView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer





