from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class meta:
        model=Student
        fields=['id','name','roll','city']