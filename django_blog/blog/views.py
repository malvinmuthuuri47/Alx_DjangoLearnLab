from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileUpdateForm

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