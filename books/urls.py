from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,  name='home'),
    path('booklist/<int:page>/', views.booklist, name='booklist'),
    path('bookdetail/<int:pk>/', views.bookdetail, name='bookdetail'),    
    path('authorlist/<int:page>/', views.authorlist, name='authorlist'),    
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path('add_author/', views.add_author, name='add_author'),
    path('search_book/', views.search_book, name='search_book'),
    path('author_detail/<int:pk>', views.author_detail, name='author_detail'),
        
]

