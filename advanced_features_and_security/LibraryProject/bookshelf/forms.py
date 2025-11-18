from django import forms
from .models import Article

class ArticleForm(forms.Modelform):
    class Meta:
        model = Article
        fields = ['title', 'body']