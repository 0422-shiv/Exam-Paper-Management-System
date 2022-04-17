from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from utils.BaseModel import DateMixin 
# Create your models here.

class Role(models.Model):
    name=models.CharField(max_length=15)
    slug = models.SlugField(max_length=70, verbose_name="slug")

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Role'

    def __str__(self) -> str:
        return self.name


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if email is None:
            raise TypeError('Users should have a Email')
        if password is None:
            raise TypeError('Password should not be none')
       
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        if email is None:
            raise TypeError('Users should have a Email')
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin,DateMixin):
    
    fullname = models.CharField(max_length=255,null=True, blank=True)  # User Fullname
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role= models.ForeignKey(Role,related_name='role',on_delete=models.CASCADE,null=True, blank=True)
        
    mobile_no = models.BigIntegerField(unique=True,null=True, blank=True)  # User contact no.
    otp = models.IntegerField(null=True, blank=True)   # email verification otp
    address = models.TextField(null=True, blank=True)
    is_terms_conditions = models.BooleanField(default=False) # Accepted terms and conditions or not
    img= models.ImageField(upload_to="profile", height_field=None, width_field=None, max_length=None,null=True,blank=True)
    assigned_course = models.ManyToManyField("data_upload.Course")
    assigned_semester =models.ManyToManyField("data_upload.Semester")
   
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email


