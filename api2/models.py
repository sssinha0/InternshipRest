from django.db import models

# Create your models here.
class employee(models.Model):
    name=models.CharField(max_length=50)
    sallry=models.IntegerField()
    address=models.CharField(max_length=100)
    status=models.BooleanField()
