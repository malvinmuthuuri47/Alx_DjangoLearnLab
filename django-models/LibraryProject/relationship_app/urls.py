from django.urls import path
from .views import list_books, LibraryDetailView, home, register
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books_fbv/', list_books, name='book_list_fbv'),
    path('books_cbv/<int:pk>', LibraryDetailView.as_view(), name='book_list_cbv'),
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]