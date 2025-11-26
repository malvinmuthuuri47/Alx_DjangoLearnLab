from django.db import models

# Create your models here.
class Author(models.Model):
    """The Author model"""
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    """The Book model"""
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} published on {self.publication_year} by {self.author}"