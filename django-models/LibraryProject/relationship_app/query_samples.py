from relationship_app import Book, Library, Author

# Query all books by a specific author
"""
1. Retrieve the author instance from the database
2. Use the author instance in a filter query in Django to retrieve books for the author
"""
author = Author.objects.get(name="Mark")
books_makr = Book.objects.filter(author=author)

author1 = Author.objects.get(name="David")
books_makr1 = Book.objects.filter(author=author1)

# List all books in a library
library_name = "ALX Sample"
Library.objects.get(name=library_name)
books = Library.books.all()

# Retrieve the librarian for a library
Library = Library.objects.get(name="ALX Sample")
Librarian = Library.librarian