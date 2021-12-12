from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,  name='home', ),
    path('booklist/<int:page>/', views.booklist, name='booklist'),
    path('bookdetail/', views.bookdetail, name='bookdetail'),    
    path('authorlist/<int:page>/', views.authorlist, name='authorlist'),    
    path('add_book/', views.add_book, name='add_book'),
        
]