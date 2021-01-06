"""ecom_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from django.views.generic.base import TemplateView
from profile.views import SignUpView, My_Profille, Profile_View, Userlist, DeleteFriend, ProfileView
from profile.views import SearchView, DeleteRequest, AcceptRequest, Friendlist, SendRequest, CancelRequest
from django.conf.urls.static import static
from django.conf import settings
from profile import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('profile/<int:pk>/', ProfileView.as_view(template_name='registration/edit_profile.html'), name='profile'),
   
    path('', TemplateView.as_view(template_name='welcome.html'), name='welcome'),
    path('signup/',SignUpView.as_view(template_name='registration/signup.html'), name='signup'),
    path('', include('posts.urls'), name='posts'),
    path('users/', Userlist.as_view(), name='users_list'),
    path('users/<slug>/',Profile_View.as_view(),name='profile_view'),
    path('frnds/',Friendlist.as_view(),name='friend_list'),
    path('users/friend-request/send/<int:id>/', SendRequest.as_view(), name='send_friend_request'),
    path('users/friend-request/delete/<int:id>/', DeleteRequest.as_view(), name='delete_friend_request'),
    path('users/friend-request/cancel/<int:id>/', CancelRequest.as_view(), name='cancel_friend_request'),
    path('users/friend-request/accept/<int:id>/', AcceptRequest.as_view(), name='accept_friend_request'),
    path('users/friend/delete/<int:id>/', DeleteFriend.as_view(), name='delete_friend'),
    path('my_profile/<slug>',My_Profille.as_view(), name='my_profile'),
    path('search_users/', SearchView.as_view(), name='search_users'),
    path('hotel_images', views.display_profile_images, name = 'profile_images'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


