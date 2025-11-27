from django.urls import path
# from .views import BookListAPI, BookDetailAPI, BookCreateAPI, BookUpdateAPI, BookDeleteAPI
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
urlpatterns = [
    path('listbooks/', BookListView.as_view()),
    path('info/<int:pk>/', BookDetailView.as_view(), name='book-info'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/<int:pk>', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/<int:pk>', BookDeleteView.as_view(), name='book-delete'),
]