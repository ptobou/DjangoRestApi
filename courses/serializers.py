from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    """This is our course serializer"""
    class Meta:
        model = Course
        fields = ('id', 'url', 'name', 'language', 'price')