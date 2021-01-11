from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views
from .views import (
    SignUpView,
    My_Profille,
    Profile_View,
    Userlist,
    DeleteFriend,
    ProfileView,
)
from .views import (
    SearchView,
    DeleteRequest,
    AcceptRequest,
    Friendlist,
    SendRequest,
    CancelRequest,
)

urlpatterns = [
    path(
        "profile/<int:pk>/",
        ProfileView.as_view(template_name="registration/edit_profile.html"),
        name="profile",
    ),
    path("", TemplateView.as_view(template_name="welcome.html"), name="welcome"),
    path(
        "signup/",
        SignUpView.as_view(template_name="registration/signup.html"),
        name="signup",
    ),
    path("", include("posts.urls"), name="posts"),
    path("users/", Userlist.as_view(), name="users_list"),
    path("users/<slug>/", Profile_View.as_view(), name="profile_view"),
    path("frnds/", Friendlist.as_view(), name="friend_list"),
    path(
        "users/friend-request/send/<int:id>/",
        SendRequest.as_view(),
        name="send_friend_request",
    ),
    path(
        "users/friend-request/delete/<int:id>/",
        DeleteRequest.as_view(),
        name="delete_friend_request",
    ),
    path(
        "users/friend-request/cancel/<int:id>/",
        CancelRequest.as_view(),
        name="cancel_friend_request",
    ),
    path(
        "users/friend-request/accept/<int:id>/",
        AcceptRequest.as_view(),
        name="accept_friend_request",
    ),
    path("users/friend/delete/<int:id>/", DeleteFriend.as_view(), name="delete_friend"),
    path("my_profile/<slug>", My_Profille.as_view(), name="my_profile"),
    path("search_users/", SearchView.as_view(), name="search_users"),
]
