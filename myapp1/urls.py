from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.usr_login,name='login'),
    path('home',views.home,name=''),
    path('usr_logout',views.usr_logout,name='usr_logout'),
    path('postblog',views.postblog,name='postblog'),
    path('blog_details/<int:id>',views.blog_details,name='blog_details')
]