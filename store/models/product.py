from django.db import models
from .catogery import Catogery
class product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    catogery=models.ForeignKey(Catogery,on_delete=models.CASCADE,default=0)
    description=models.CharField(max_length=200,default='')
    image=models.ImageField(upload_to='upload/product/')

    @staticmethod
    def get_all_product():
        return product.objects.all()