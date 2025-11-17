from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.list_articles),
    path('articles/create/', views.create_article),
    path('articles/<int:article_id>/edit/', views.edit_article),
    path('articles/<int:article_id>/delete/', views.delete_article),
]