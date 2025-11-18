from django import forms
from .models import Article

class ExampleForm(forms.Modelform):
    class Meta:
        model = Article
        fields = ['title', 'body']