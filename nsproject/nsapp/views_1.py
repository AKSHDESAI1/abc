from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Instructor, Course
from nsapp.serializers import InstructorSerializer, CourseSerializer

from rest_framework import permissions
from rest_framework.authentication import BasicAuthentication
# Create your views here.


class InstructorListView(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()


class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()


class CourseListView(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
