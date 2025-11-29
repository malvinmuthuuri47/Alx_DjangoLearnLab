from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import BookSerializer
from .models import Book
from django.urls import reverse_lazy
from django.db.models import Q
from django_filters import rest_framework
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
# class BookListAPI(ListAPIView):
#     """
#     A DRF class-based view to list all books in the database
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

COMMON_FILTER_BACKENDS = [
    DjangoFilterBackend,
    filters.SearchFilter,
    filters.OrderingFilter,
]
class BookListView(ListView):
    """
    A class-based view to list all books in the database
    """
    model = Book
    template_name = 'api/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        """
        This method defines the ordering configuration for the Book model on the fields listed in the allowed fields list.

        The method also defines search functionality for the book model based on the book title and author name.

        The method also sets up filtering on the Books by using the author name field.
        """
        queryset = super().get_queryset()

        # filtering
        author = self.request.GET.get("author")
        if author:
            queryset = queryset.filter(author__name__icontains=author)
        
        # search functionality
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(author__name__icontains=search)
            )
        
        # ordering functionality
        order = self.request.GET.get("order")
        allowed_fields = ["title", "publication_year"]
        if order in allowed_fields:
            queryset = queryset.order_by(order)
        
        return queryset

# class BookDetailAPI(RetrieveAPIView):
#     """
#     A DRF class-based view to show the details of a single book
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated]
class BookDetailView(DetailView):
    """
    A class-based view to show the details of a single book
    """
    model = Book
    template_name = 'api/book_detail.html'
    context_object_name = 'book'

# class BookCreateAPI(ListCreateAPIView):
#     """
#     A class-based view to create a new book requiring a user
#     to be logged in
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated]
class BookCreateView(CreateView):
    """
    A class-based view to create a new book
    """
    model = Book
    fields = '__all__'
    template_name = 'api/book_create.html'
    success_url = reverse_lazy('book-list')

# class BookUpdateAPI(RetrieveUpdateAPIView):
#     """
#     A class-based view that updates a book instance requiring
#     a user to be logged in
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated]
class BookUpdateView(UpdateView):
    """
    A class-based view that updates a book instance
    """
    model = Book
    fields = ['title', 'author']
    template_name = 'api/book_update.html'
    success_url = reverse_lazy('book-list')


# class BookDeleteAPI(RetrieveDestroyAPIView):
#     """
#     A class-based view that deletes a book instance requiring
#     a user to be logged in also
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticated]
class BookDeleteView(DeleteView):
    """
    A class-based view that deletes a book instance
    """
    model = Book
    success_url = reverse_lazy('book-list')
    template_name = 'api/book_delete.html'
    context_object_name = 'book'
