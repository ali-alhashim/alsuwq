from django.db import models
from category.models import Category
from django.urls import reverse
from user.models import User
# Create your models here.

class Product(models.Model):
      product_name           = models.CharField(max_length=255, unique=True)
      slug                   = models.SlugField(max_length=255, unique=True)
      description            = models.TextField(blank=True)
      price                  = models.DecimalField(max_digits=13, decimal_places=2, default=0.00)

      image_1                 = models.ImageField(upload_to='photos/products', blank=True)
      image_2                 = models.ImageField(upload_to='photos/products', blank=True)
      image_3                 = models.ImageField(upload_to='photos/products', blank=True)
      image_4                 = models.ImageField(upload_to='photos/products', blank=True)

      stock                   = models.PositiveIntegerField(default=0)
      is_available            = models.BooleanField(default=False)
      category                = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
      created_date            = models.DateTimeField(auto_now_add=True)
      last_update             = models.DateTimeField(auto_now=True)

      def __str__(self):
            return self.product_name
      
      def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
      


class ReviewRating(models.Model):
     product = models.ForeignKey(Product, on_delete=models.CASCADE)
     user    = models.ForeignKey(User, on_delete=models.CASCADE)
     subject = models.CharField(max_length=100, blank=True)
     review  = models.TextField(max_length=500, blank=True)
     rating  = models.FloatField()
     ip      = models.CharField(max_length=20, blank=True)
     status  = models.BooleanField(default=True)
     created_date            = models.DateTimeField(auto_now_add=True)
     last_update             = models.DateTimeField(auto_now=True)

     def __str__(self):
          return self.subject
