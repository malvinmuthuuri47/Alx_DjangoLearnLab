# CREATE Django Markdown file

This file contains all the code that uses the django shell to create an instance of the model

from .models import Book

book_one = Book(title="1984", author="George Orwell", publication_year=1949)

book_one.save() 
