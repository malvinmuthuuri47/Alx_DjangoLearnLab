# UPDATE Django Markdown file

This file contains all the code that uses the django shell to update a django instance of the model

from .models import Book

book = Book.objects.get(pk=1)

book.title = "Nineteen Eighty-Four"

book.save()
