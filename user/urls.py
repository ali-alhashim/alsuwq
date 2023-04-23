from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('register/',views.register, name='register'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    path('resetPassword/<uidb64>/<token>', views.resetPassword, name='resetPassword'),
    path('your_addresses/', views.your_addresses, name='your_addresses'),
]