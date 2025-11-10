from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.author.name}"
    
class Library(models.Model):
    name = models.CharField(max_length=64)
    books = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"Library {self.name} has book {self.books.title}"
    
class Librarian(models.Model):
    name = models.CharField(max_length=64)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"Librarian {self.name} looks after library {self.library.name}"