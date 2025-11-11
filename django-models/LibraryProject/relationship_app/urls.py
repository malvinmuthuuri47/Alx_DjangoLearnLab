from django.urls import path
from . import views
from .views import list_books
from . import admin_view, librarian_view, member_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('books_fbv/', list_books, name='book_list_fbv'),
    path('books_cbv/<int:pk>', views.LibraryDetailView.as_view(), name='book_list_cbv'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin-dashboard/', admin_view.admin_view, name='admin_view'),
    path('librarian-dashboard/', librarian_view.librarian_view, name='librarian_view'),
    path('member-dashboard/', member_view.member_view, name='member_view'),
]