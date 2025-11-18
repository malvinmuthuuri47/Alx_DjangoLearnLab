from django import forms
from .models import Article

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body']