from rest_framework import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Course, CourseSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def courseListView(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        courseSerializer = CourseSerializer(courses, many=True)
        return Response(courseSerializer.data)
    elif request.method == 'POST':
        courseSerializer = CourseSerializer(data=request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(courseSerializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def courseDetailView(request, pk):
    try:
        courses = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        courseSerializer = CourseSerializer(courses)
        return Response(courseSerializer.data)
    elif request.method == 'PUT':
        courseSerializer = CourseSerializer(courses, data=request.data)
        if courseSerializer.is_valid():
            courseSerializer.save()
            return Response(courseSerializer.data)
        else:
            return Response(courseSerializer.errors)
    elif request.method == 'DELETE':
        courses.delete()
        return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
