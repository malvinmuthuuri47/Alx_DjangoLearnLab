from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books_fbv/', list_books, name='book_list_fbv'),
    path('books_cbv/<int:pk>', LibraryDetailView.as_view(), name='book_list_cbv'),
]