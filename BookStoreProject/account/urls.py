from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('log in/', views.user_login, name='login'),
    path('log out/', views.user_logout, name='logout'),
    path('profile/', views.my_profile, name='my_profile'),
]