from django.db import models
from user.models import User
from product.models import Product
# Create your models here.

class Favorites(models.Model):
    name       = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    user       = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name




class FavoritesItem(models.Model):
    favorites = models.ForeignKey(Favorites, on_delete=models.CASCADE)
    product   = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.product