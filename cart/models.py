from django.db import models
from product.models import Product
from user.models import User
# Create your models here.

class Cart(models.Model):
    cart_id    = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product   = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart      = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    user      = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity  = models.PositiveIntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.product