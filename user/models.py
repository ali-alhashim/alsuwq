from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, name, email, mobile, address, password=None):
        if not email:
            raise ValueError('you must enter email address !')
        user = self.model(
                           email = self.normalize_email(email),
                           name  = name,
                           mobile = mobile,
                           address = address
                         )
        user.set_password(password)
        user.save(using= self._db)
        return user
    
    def create_superuser(self, name, email, mobile, address=None, password=None):
        if not email:
            raise ValueError('you must enter email address !')
        user = self.model(
                        email = self.normalize_email(email),
                        name  = name,
                        mobile = mobile,
                        address = address
                        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff     = True
        user.is_admin     = True
        user.is_active    = True
        user.save(using= self._db)
        return user


class User(AbstractBaseUser):
    name             = models.CharField(max_length=255)
    email            = models.EmailField(max_length=255, unique=True)
    mobile           = models.CharField(max_length=50)
    address          = models.TextField(max_length=500, blank=True, null=True)
    is_seller        = models.BooleanField(default=False)
    national_identity_number = models.CharField(max_length=50, blank=True, null=True)

    date_joined      = models.DateTimeField(auto_now_add=True)
    last_login       = models.DateTimeField(auto_now_add=True)
    is_admin         = models.BooleanField(default=False)
    is_staff         = models.BooleanField(default=False)
    is_active        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD   = 'email'
    REQUIRED_FIELDS  = ['name', 'mobile']
    objects = MyUserManager()
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    

class UserAddresses(models.Model):
    created_date  = models.DateTimeField(auto_now_add=True)
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    title         = models.CharField(max_length=250, default='Address title')
    is_default    = models.BooleanField(default=False)
    country       = models.CharField(max_length=255, default='Saudi Arabia')
    full_name     = models.CharField(max_length=255, default='first and last name')
    mobile        = models.CharField(max_length=50, default='00966')
    city          = models.CharField(max_length=255, blank=True, null=True)
    area          = models.CharField(max_length=255, blank=True, null=True)
    province      = models.CharField(max_length=255, default='Eastern Province')
    nearest_landmark = models.CharField(max_length=255, blank=True, null=True)
    note          = models.TextField(max_length=500, blank=True, null=True)

