from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        permissions = [
            ("can_add_book", "Can add a book"),
            ("can_change_book", "Can change a book"),
            ("can_delete_book", "Can delete a book"),
        ]

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

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Member')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()