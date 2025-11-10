from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"Book title: {self.title}"
        # return f"title -> {self.title} Author -> {self.author} Publication_year ->   {self.publication_year}"
