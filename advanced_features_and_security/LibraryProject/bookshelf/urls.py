from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.book_list),
    path('articles/create/', views.create_article),
    path('articles/<int:article_id>/edit/', views.edit_article),
    path('articles/<int:article_id>/delete/', views.delete_article),
    path('articles/new/', views.createArticle, name='create_article'),
]