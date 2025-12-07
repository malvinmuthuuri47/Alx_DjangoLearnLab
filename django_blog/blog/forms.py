from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from django.core.exceptions import ValidationError

# custom registration form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter your email address")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# profile view form
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter post title'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Write yout post content here...',
                'rows': 10
            }),
            'tags': forms.TextInput(attrs={
                'placeholder': 'Enter tags separated by commas',
                'data-role': 'tagsinput'
            }),
        }
        labels = {
            'tags': TagWidget(),
        }
        help_texts = {
            'tags': 'Separate tags with commas'
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your comment here...',
                'rows': 4
            }),
        }
        labels = {
            'content': 'Your Comment'
        }
    
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content.strip()) == 0:
            raise forms.validationError("Comment cannot be empty.")
        return content