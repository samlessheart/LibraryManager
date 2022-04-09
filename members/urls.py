from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('update/', views.update, name='user-update'), 
    path('signout/', views.signout, name='signout'),
    path('all_members/', views.all_members, name='all_members'), 

]