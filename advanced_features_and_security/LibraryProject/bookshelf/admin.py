from django.contrib import admin
from .models import Book, CustomUser

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title',)
    list_filter = ('title',)

class CustomUserAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
