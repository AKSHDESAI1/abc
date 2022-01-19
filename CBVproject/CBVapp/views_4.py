from django.shortcuts import render, resolve_url
from rest_framework import serializers
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course, CourseSerializer
from rest_framework import status
from django.http import Http404
from rest_framework import mixins, generics
# Create your views here.

# viewSet
from rest_framework.viewsets import ViewSet


class CourseViewSet(ViewSet):
    def list(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def retrieve(self, request, pk):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return response(status=status.HTTP_404_NOT_FOUND)

        serializer = CourseSerializer(course)
        return Response(serializer.data)


# class CourseListView(generics.ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

# class CourseDetailView(generics.RetrieveDestroyAPIView):
    # queryset = Course.objects.all()
    # serializer_class = CourseSerializer


# class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer


# class CourseDetailView(generics.RetrieveUpdateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
