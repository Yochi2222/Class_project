from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('search/', views.search_books, name='search_books'),
    path('add/', views.add_book, name='add_book'),
]
