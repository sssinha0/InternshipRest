from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaserUserAdmin
# Register your models here.
from .models import NewUser
class UserAdmin(BaserUserAdmin):
    list_display=('email','admin')
    list_filter=('admin',)
    fieldsets = (
        (None, {
            "classes": ('wide',),
            'fields':('email','password','password2')}),
            ('personal info',{'fields':()}),
            ('permissions',{'fields':('admin',)}),
    )
    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('email','password','password2')}
        ),
    )
    search_fields=('email',)
    ordering=('email',)
    filter_horizontal=()
admin.site.register(NewUser,UserAdmin)



'''

from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager
)
# Create your models here
class UserManager(BaseUserManager):
    def create_user(self,email,company_name,phone,password=None):
        if not email:
            raise ValueError("user must have an email address")
        if not company_name:
            raise ValueError("company name id is required")
        if not phone:
            raise ValueError("please provide phone number")
        user=self.model(
            email=self.normalize_email(email),
            company_name=company_name,
            phone=phone

        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self,email,password=None):
        user=self.create_user(
            email,
            password=password
        )
        user.staff=True
        user.save(using=self._db)
        return user
    def create_superuser(self,email,company_name,phone,password=None):
        user=self.create_user(
            email=email,
            company_name=company_name,
            phone=phone,
            password=password
        )
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class NewUser(AbstractBaseUser):
    objects=UserManager()
    email=models.EmailField(max_length=50,unique=True)
    comapany_name=models.CharField(max_length=500,unique=True)
    phone=models.CharField(max_length=50)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['company_name','phone']

    def __str__(self):
        return self.comapany_name
    



    # active=models.BooleanField(default=True)
    # staff=models.BooleanField(default=False)
    # admin=models.BooleanField(default=False)
    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_staff
    
    
    @property
    def is_admin(self):
        return self.is_admin
    @property
    def is_active(self):
        return self.is_active

'''