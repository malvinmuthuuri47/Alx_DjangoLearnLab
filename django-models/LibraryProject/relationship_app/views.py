from django.shortcuts import render
from django.views.generic import ListView
from .models import Book, Library

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class BookListView(ListView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'libraries'   