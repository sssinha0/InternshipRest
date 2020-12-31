from django.contrib import admin
from  .models.product import product
from  .models.catogery import Catogery
# Register your models here.
class Adminproduct(admin.ModelAdmin):
    list_display=['name','price','catogery']
admin.site.register(product,Adminproduct)

class AdminCatogery(admin.ModelAdmin):
    list_display=['name']
admin.site.register(Catogery,AdminCatogery)