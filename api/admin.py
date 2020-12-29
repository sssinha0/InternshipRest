from django.contrib import admin
<<<<<<< HEAD

# Register your models here.
=======
from .models import Student
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']
>>>>>>> firsit commit
