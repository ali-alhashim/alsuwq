from django.db import models
from user.models import User
# Create your models here.

class Store(models.Model):
    created_date = models.DateField(auto_now_add=True)
    store_name   = models.CharField(max_length=255, default='')
    seller_user  = models.ForeignKey(User, on_delete=models.CASCADE)
    is_professional_plan = models.BooleanField(default=False)          ## one store can managed by many users
    is_individual_plan   = models.BooleanField(default=True)           ## only one user manage the store


