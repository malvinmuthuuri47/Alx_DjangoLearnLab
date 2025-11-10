from django.urls import path
from .views import book_list, BookListView

urlpatterns = [
    path('books_fbv/', book_list, name='book-list'),
    path('books_cbv/', BookListView.as_view(), name='book_list'),
]