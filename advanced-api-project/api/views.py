from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Book
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class BookListView(ListView):
    """
    A class-based view to list all books in the database
    """
    model = Book
    template_name = 'api/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    """
    A class-based view to show the details of a single book
    """
    model = Book
    template_name = 'api/book_detail.html'
    context_object_name = 'book'

class BookCreateView(LoginRequiredMixin, CreateView):
    """
    A class-based view to create a new book requiring a user
    to be logged in
    """
    model = Book
    fields = '__all__'
    template_name = 'api/book_create.html'
    success_url = reverse_lazy('book-list')

class BookUpdateView(LoginRequiredMixin, UpdateView):
    """
    A class-based view that updates a book instance requiring
    a user to be logged in
    """
    model = Book
    fields = ['title', 'author']
    template_name = 'api/book_update.html'
    success_url = reverse_lazy('book-list')

class BookDeleteView(LoginRequiredMixin, DeleteView):
    """
    A class-based view that deletes a book instance requiring
    a user to be logged in also
    """
    model = Book
    success_url = reverse_lazy('book-list')
    template_name = 'api/book_delete.html'
    context_object_name = 'book'