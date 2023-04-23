from django.urls import path
from . import views
urlpatterns = [

     path('your_orders/',views.your_orders, name='your_orders'),
     path('payselect/', views.payselect, name='payselect'),
]