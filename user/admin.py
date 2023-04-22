from django.contrib import admin
from .models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    
    list_display        = ('name', 'email', 'mobile', 'is_active')
    search_fields       = ('name','email', 'mobile')
admin.site.register(User, UserAdmin)
