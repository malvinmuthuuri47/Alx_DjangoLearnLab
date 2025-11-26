from .models import Book, Author
from rest_framework import serializers
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    """
    The serializer for the Book model
    """
    class Meta:
        model = Book
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    """
    The serializer for the Author model with a nested serializer for the books associated with the author
    """
    books = BookSerializer()
    
    class Meta:
        model = Author
        fields = ['name', 'books']
    
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(f"Publication year cannot be in the future (>{current_year}).")
        return value