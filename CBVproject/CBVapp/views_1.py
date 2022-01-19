from django.shortcuts import render, resolve_url
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course, CourseSerializer
from rest_framework import status
from django.http import Http404
from rest_framework import mixins, generics
# Create your views here.


class CourseListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class CourseDetailView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)


# class CourseListView(APIView):
#     def get(self, request):
#         courses = Course.objects.all()
#         serializer = CourseSerializer(courses, many=True)
#         # json = serializer.data
#         return Response(serializer.data)

#     def post(self, request):
#         courseSerializer = CourseSerializer(data=request.data)
#         if courseSerializer.is_valid():
#             courseSerializer.save()
#             return Response(courseSerializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(courseSerializer.errors)


# class CourseDetailView(APIView):

#     def get_course(self, pk):
#         try:
#             course = Course.objects.get(pk=pk)
#             return course
#         except Course.DoesNotExist:
#             # return Response(status=status.HTTP_400_BAD_REQUEST)
#             raise Http404

#     def get(self, request, pk):
#         course = self.get_course(pk)
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)

#     def delete(self, request, pk):
#         course = self.get_course(pk)
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     def put(self, request, pk):
#         courses = self.get_course(pk)
#         courseSerializer = CourseSerializer(courses, data=request.data)
#         if courseSerializer.is_valid():
#             courseSerializer.save()
#             return Response(courseSerializer.data)
#         else:
#             return Response(courseSerializer.errors)
