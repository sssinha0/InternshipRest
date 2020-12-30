from django.contrib import admin
from .models import employee
# Register your models here.
admin.site.register(employee)
class employeeAdmin(admin.ModelAdmin):
    list_display=['id','name','address''sallry','status']

