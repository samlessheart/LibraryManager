from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [        
    path('borrow/<int:pk>/', views.borrow, name='borrow'),    
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard1/', views.dashboard1, name='dashboard1'),
    path('profile/', views.profile, name='profile'),
    path('book_return/<int:pk>/', views.book_return, name='book_return'),
    
        
]