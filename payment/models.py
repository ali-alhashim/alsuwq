from django.db import models
from user.models import User
# Create your models here.

## each user has many credit card
class CreditCard(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    cvv          = models.CharField(max_length=10, blank=True, null=True)
    expiry_date  = models.DateField(blank=True,null=True)
    card_number  = models.CharField(max_length=200, blank=True, null=True)
    name_on_card = models.CharField(max_length=255, blank=True, null=True)


