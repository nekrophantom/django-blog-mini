from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),

    path('blog/<int:pk>/', views.blogPage, name='blog'),
    path('create-blog/', views.createBlogPage, name='create-blog'),
    path('my-blog/<int:pk>/', views.userBlogPage, name='my-blog'),
    path('update-blog/<int:pk>/', views.updateBlogPage, name='update-blog'),
    path('delete-blog/<int:pk>/', views.deleteBlogPage, name='delete-blog'),
]
