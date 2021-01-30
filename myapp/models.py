from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser,BaseUserManager
)
# Create your models here
class UserManager(BaseUserManager):
    def create_user(self,email,company,phone,password=None):
        if not email:
            raise ValueError("user must have an email address")
        user=self.model(
            email=self.normalize_email(email),
            company_name=company,
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
    def create_superuser(self,email,company,phone,password=None):
        user=self.create_user(
            email=email,
            phone=phone,
            company=company,
            password=password
        )
        user.staff=True
        user.admin=True
        user.save(using=self._db)
        return user


class NewUser(AbstractBaseUser):
    objects=UserManager()
    email=models.EmailField(max_length=50,unique=True)
    company=models.CharField(verbose_nammax_length=50,unique=True)
    phone=models.CharField(max_length=50,unique=True)
    # date_joine=models.DateTimeField(auto_now_add=True)
    # last_login=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)
    staff=models.BooleanField(default=False)
    admin=models.BooleanField(default=False)
    superuser=models.BooleanField(default=False)
    USERNAME_FIELD='email'
    REQUIRED_FIELD=['company','phone']


    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email
    def __str__(self):
        return self.email
    def has_perm(self,perm,obj=None):
        return True
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    @property
    def is_active(self):
        return self.active
