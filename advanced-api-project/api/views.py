from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializers import BookSerializer
from .models import Book

# Create your views here.
class BookListAPI(ListAPIView):
    """
    A class-based view to list all books in the database
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookDetailAPI(RetrieveAPIView):
    """
    A class-based view to show the details of a single book
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookCreateAPI(ListCreateAPIView):
    """
    A class-based view to create a new book requiring a user
    to be logged in
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookUpdateAPI(RetrieveUpdateAPIView):
    """
    A class-based view that updates a book instance requiring
    a user to be logged in
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteAPI(RetrieveDestroyAPIView):
    """
    A class-based view that deletes a book instance requiring
    a user to be logged in also
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
