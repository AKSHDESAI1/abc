from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Instructor, Course
from nsapp.serializers import InstructorSerializer, CourseSerializer

from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
from rest_framework.authentication import BasicAuthentication, TokenAuthentication

from rest_framework.authtoken.models import Token

# Create your views here.

# users = User.objects.all()
# # print(11)
# for user in users:
#     token = Token.objects.get_or_create(user=user)
#     print(token)


class WritebyAdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method == 'GET':
            return True
        if request.method == 'POST' or request.method == 'PUT' or request.method == 'DELETE':
            if user.is_superuser:
                return True
        return False


class InstructorListView(generics.ListCreateAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()


class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstructorSerializer
    queryset = Instructor.objects.all()


class CourseListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated, WritebyAdminOnlyPermission]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
