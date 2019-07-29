from django.urls import path

from .views import emailView


app_name = 'contact'
urlpatterns = [
    path('', emailView, name='email'),
]