from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileUpdateForm, PostForm, CommentForm
from .models import Post, Comment
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse

# registration view
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): # check if data is valid
            user = form.save()  # create the user
            login(request, user)    # log the user in autmoatically
            messages.success(request, f'Welcome {user.username}! Your account has been created')
            return redirect('profile')  # send them to their profile
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'blog/register.html', {'form': form})

# logout view
def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('login')

# profile view
@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save() # save the updated information
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        # show the form pre-filled with current user data
        form = ProfileUpdateForm(instance=request.user)
    
    return render(request, 'blog/profile.html', {'form': form})

class PostListView(ListView):
    '''This is a list view, showing all posts'''
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

class PostDetailView(DetailView):
    '''This is a detail view showing a single post'''
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['comment_form'] = CommentForm()
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    '''
    This is a View that allows creation of a new post and the user
    must be logged in
    '''
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    # set author to the logged-in user before saving
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # redirect to the newly created post after success
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.kwargs['post_id']})
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    '''View to update an existing post'''
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    # check if the current user is the author
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    # redirect to the updated post after success
    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={'pk': self.object.pk})

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts')

    # check if the current user is the author
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# Comment Views
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        messages.success(self.request, 'Your comment has been posted!')
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk']})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
    def get_success_url(self):
        messages.success(self.request, 'Your comment has been updated!')
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
    def get_success_url(self):
        messages.success(self.request, 'Your comment has been deleted.')
        return reverse('post-detail', kwargs={'pk': self.object.post.pk})