from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('listbooks/', BookListView.as_view(), name='book-list'),
    path('info/<int:pk>/', BookDetailView.as_view(), name='book-info'),
    path('create/', BookCreateView.as_view(), name='book-create'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='book-update'),
    path('delete/<int:pk>', BookDeleteView.as_view(), name='book-delete'),
]