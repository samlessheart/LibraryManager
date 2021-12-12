from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,  name='home', ),
    path('booklist/<int:page>/', views.booklist, name='booklist'),
    path('bookdetail/', views.bookdetail, name='bookdetail'),
    path('borrow/<int:pk>/', views.borrow, name='borrow'),
    path('authorlist/<int:page>/', views.authorlist, name='authorlist'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard1/', views.dashboard1, name='dashboard1'),
    path('profile/', views.profile, name='profile'),
    path('add_book/', views.add_book, name='add_book'),
        
]