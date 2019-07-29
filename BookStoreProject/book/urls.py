from django.urls import path
from . import views


app_name = 'book'
urlpatterns = [
  path('shop/', views.book_list, name='bookList'),
  path('single/<int:id>', views.single_book, name='single'),
  path('search/', views.search, name='search_results'),
]
