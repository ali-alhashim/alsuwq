from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
      list_display  = ('product_name','description', 'price', 'stock', 'is_available', 'category', 'last_update')
      search_fields = ('product_name','description', 'stock', 'is_available', 'category', 'last_update')
      ordering      = ('last_update',)
      prepopulated_fields = {'slug':('product_name',)}
admin.site.register(Product, ProductAdmin)
