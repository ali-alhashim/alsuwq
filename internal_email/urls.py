from django.urls import path
from . import views
urlpatterns = [
    path('your_email', views.your_email, name='your_email'),
]