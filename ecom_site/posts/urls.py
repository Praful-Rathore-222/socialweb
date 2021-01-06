from django.contrib import admin
from django.urls import path, include
from . import views
from .views import PostUpdateView, PostListView, UserPostListView, CreatePost

urlpatterns=[
	path('home/', PostListView.as_view(), name='home'),
	path('post/new/', views.CreatePost.as_view(), name='post-create'),
	path('post/<int:pk>/', views.post_detail, name='post-detail'),
	path('like/', views.like, name='like'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete/', views.DeletePost.as_view(), name='post-delete'),
	path('user_posts/<str:username>', UserPostListView.as_view(), name='user-posts'),
	
	
]
