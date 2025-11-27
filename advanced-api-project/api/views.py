from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import BookSerializer
from .models import Book
from django.urls import reverse_lazy

# Create your views here.
# class BookListAPI(ListAPIView):
#     """
#     A DRF class-based view to list all books in the database
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
class BookListView(ListView):
    """
    A class-based view to list all books in the database
    """
    models = Book
    template_name = 'api/book_list.html'
    context_object_name = 'books'

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
