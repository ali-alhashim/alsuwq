from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
]