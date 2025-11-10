from django.urls import path
from .views import book_list, BookListView

urlpatterns = [
    path('books_fbv/', book_list, name='book_list_fbv'),
    path('books_cbv/<int:pk>', BookListView.as_view(), name='book_list_cbv'),
]