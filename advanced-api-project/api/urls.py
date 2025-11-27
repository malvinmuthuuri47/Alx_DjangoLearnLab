from django.urls import path
from .views import BookListAPI, BookDetailAPI, BookCreateAPI, BookUpdateAPI, BookDeleteAPI

urlpatterns = [
    path('listbooks/', BookListAPI.as_view()),
    path('info/<int:pk>/', BookDetailAPI.as_view(), name='book-info'),
    path('books/create/', BookCreateAPI.as_view(), name='book-create'),
    path('books/update/<int:pk>', BookUpdateAPI.as_view(), name='book-update'),
    path('books/delete/<int:pk>', BookDeleteAPI.as_view(), name='book-delete'),
]