# CREATE Django Markdown file

This file contains all the code that uses the django shell to create an instance of the model

from .models import Book

Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
