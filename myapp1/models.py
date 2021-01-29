from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
class BlogPost(models.Model):
    username=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    des=models.TextField(max_length=200)
    date=models.DateTimeField(auto_now_add=True,null=True)

