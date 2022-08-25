from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib import admin
from . import views




urlpatterns = [
    path('book_list/', views.book_list, name='book_list'),
    path('book_detail/<int:pk>/', views.book_detail, name='book_detail'),
    path('book_det/<int:pk>/', views.book_det, name='book_det'),

    path('book_create/', views.book_create, name='book_create'),
    path('user_list/', views.user_list, name='user_list'),
    path('user_det/<int:pk>/', views.user_det, name='user_det'),
    path('borrow/<int:pk>/', views.borrow, name='borrow_book'),
    path('return_book/<int:pk>/', views.return_book, name='return_book'),
    path('passbook/', views.passbook, name='passbook'),


    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]