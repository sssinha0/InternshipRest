from django.contrib import admin
from .models import Student
from .serializers import StudentSerializers
# Register your models here.
admin.site.register(Student)
