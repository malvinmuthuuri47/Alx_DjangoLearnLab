from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books_fbv/', views.list_books, name='book_list_fbv'),
    path('books_cbv/<int:pk>', views.LibraryDetailView.as_view(), name='book_list_cbv'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]