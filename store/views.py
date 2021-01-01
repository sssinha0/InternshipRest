from django.shortcuts import render
from .models.product import product
# Create your views here.
def index(request):
    prod=product.get_all_product()
    return render(request,'index.html',{'product':prod})