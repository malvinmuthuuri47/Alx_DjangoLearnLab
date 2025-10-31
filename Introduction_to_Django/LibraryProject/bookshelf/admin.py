from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title',)
    list_filter = ('title',)

# Register your models here.
admin.site.register(Book, BookAdmin)
