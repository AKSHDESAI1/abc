from django.db import models
from django.db.models import fields
from rest_framework import serializers
# Create your models here.


# class Instructor(models.Model):
#     name = models.CharField(max_length=30)
#     email = models.EmailField()

#     def __str__(self):
#         return self.email


class Course(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=40)
    price = models.IntegerField()
    discount = models.IntegerField(default=0)
    duration = models.FloatField()


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


# class InstructorSerializer(serializers.ModelSerializer):
#     courses1 = CourseSerializer(read_only=True, many=True)
#     class Meta:
#         model = Instructor
#         fields = '__all__'
