# RETRIEVE Django Markdown file

This file contains all the code that uses the django shell to retrieve a django instance of the model

from .models import Book

book_one = Book.objects.get(pk=1)
