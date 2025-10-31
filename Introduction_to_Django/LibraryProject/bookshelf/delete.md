# DELETE Django Markdown file

This file contains all the code that uses the django shell to delete a django instance of the model

from bookshell.models import Book

book = Book.objects.get(pk=1)

book.delete()
