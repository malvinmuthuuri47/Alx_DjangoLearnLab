from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Book
from .models import Library
from .models import Author

# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

@csrf_exempt
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')

        if not title or not author_id:
            return HttpResponse('Missing title or author_id', status=400)
        
        try:
            author = Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return HttpResponse("Author not found", status=404)
        
        book = Book.objects.create(title=title, author=author)
        return HttpResponse(f"Book '{book.title}' added successfully", status=201)
    
    return HttpResponse("Only Post method allowed", status=405)

@csrf_exempt
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=pk)
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')

        if title:
            book.title = title
        
        if author_id:
            try:
                author = Author.objects.get(id=author_id)
                book.author = author
            except Author.DoesNotExist:
                return HttpResponse("Author not found", status=404)
        
        book.save()
        return HttpResponse(f"Book {book.id} updated successfully")
    
    return HttpResponse("Only POST method allowed", status=405)

@csrf_exempt
@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    if request.method == 'POST':
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return HttpResponse(f"Book {pk} deleted successfully")
    
    return HttpResponse("Only POST method allowed", status=405)

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def home(request):
    return render(request, 'relationship_app/logout.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! You can now log in")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Librarian logic
def is_librarian(user):
    """
    This function checks for a user's session and the appropriate
    role to access the view
    """
    return user.is_authenticated and user.userprofile.role == 'Librarian'

@user_passes_test(is_librarian)
@login_required
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member logic
def is_member(user):
    """
    This function checks for a user's session and the appropriate
    role to access the view
    """
    return user.is_authenticated and user.userprofile.role == 'Member'

@user_passes_test(is_member)
@login_required
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# Admin logic
def is_admin(user):
    """
    This function checks for a user's session and the appropriate
    role to access the view
    """
    return user.is_authenticated and user.userprofile.role == 'Admin'

@user_passes_test(is_admin)
@login_required
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')