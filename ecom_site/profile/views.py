from django.shortcuts import render
from django.views import View

# from django.views.generic import
from django.views.generic import CreateView, UpdateView, ListView, DetailView
from .forms import SignUpForm, ProfileForm
from django.views import generic
from django.urls import reverse_lazy
from .models import User

from django.views import View
from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from posts.models import Post
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.conf import settings
from django.http import HttpResponseRedirect
from .models import Profile, FriendRequest
import random
from django.views.generic.base import TemplateView

User = get_user_model()


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ProfileView(UpdateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy("home")
    template_name = "registration/edit_profile.html"


class Userlist(LoginRequiredMixin, View):
    def get(self, request):
        users = Profile.objects.exclude(user=self.request.user)
        sent_friend_requests = FriendRequest.objects.filter(from_user=self.request.user)
        sent_to = []
        friends = []
        for user in users:
            friend = user.friends.all()
            for f in friend:
                if f in friends:
                    friend = friend.exclude(user=f.user)
            friends += friend
        my_friends = request.user.profile.friends.all()
        for i in my_friends:
            if i in friends:
                friends.remove(i)
        if request.user.profile in friends:
            friends.remove(request.user.profile)
        random_list = random.sample(list(users), min(len(list(users)), 10))
        for r in random_list:
            if r in friends:
                random_list.remove(r)
        friends += random_list
        for i in my_friends:
            if i in friends:
                friends.remove(i)
        for se in sent_friend_requests:
            sent_to.append(se.to_user)
        context = {"users": friends, "sent": sent_to}
        return render(request, "registration/users_list.html", context)


class Friendlist(ListView):
<<<<<<< HEAD
    def get(self, request):
        p = request.user.profile
        friends = p.friends.all()
        context = {"friends": friends}
        return render(request, "registration/friend_list.html", context)
=======
    def get (self, request):
        p = request.user.profile
        friends = p.friends.all()
        context={
            'friends': friends
        }
        return render(request, "registration/friend_list.html", context)


>>>>>>> da5a722df9e7d65b809bbdac668dcc14dae16615


class SendRequest(LoginRequiredMixin, View):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        frequest, created = FriendRequest.objects.get_or_create(
            from_user=self.request.user, to_user=user
        )
        return HttpResponseRedirect("/users/{}".format(user.profile.slug))


class CancelRequest(LoginRequiredMixin, View):
    def get(self, request, id):
        user = get_object_or_404(User, id=id)
        frequest = FriendRequest.objects.filter(
            from_user=self.request.user, to_user=user
        ).first()
        frequest.delete()
        return HttpResponseRedirect("/users/{}".format(user.profile.slug))


class AcceptRequest(LoginRequiredMixin, View):
    def get(self, request, id):
        from_user = get_object_or_404(User, id=id)
        frequest = FriendRequest.objects.filter(
            from_user=from_user, to_user=self.request.user
        ).first()
        user1 = frequest.to_user
        user2 = from_user
        user1.profile.friends.add(from_user)
        user2.profile.friends.add(self.request.user)
<<<<<<< HEAD

=======
>>>>>>> da5a722df9e7d65b809bbdac668dcc14dae16615
        if FriendRequest.objects.filter(
            from_user=request.user, to_user=from_user
        ).first():
            request_rev = FriendRequest.objects.filter(
                from_user=self.request.user, to_user=from_user
            ).first()
            request_rev.delete()
        frequest.delete()
        return HttpResponseRedirect("/users/{}".format(request.user.profile.slug))


class DeleteRequest(LoginRequiredMixin, View):
    def get(self, request, id):
        from_user = get_object_or_404(User, id=id)
        frequest = FriendRequest.objects.filter(
            from_user=from_user, to_user=self.request.user
        ).first()
        frequest.delete()
        return HttpResponseRedirect("/users/{}".format(request.user.profile.slug))


class DeleteFriend(LoginRequiredMixin, View):
    def get(self, request, id):
        user = self.request.user
        friend = get_object_or_404(User, id=id)
        user.profile.friends.remove(friend)
        friend.profile.friends.remove(user)
        return HttpResponseRedirect("/users/{}".format(friend.profile.slug))
<<<<<<<
=======


>>>>>>> da5a722df9e7d65b809bbdac668dcc14dae16615


class Profile_View(LoginRequiredMixin, View):
    def get(self, request, slug):
        p = Profile.objects.filter(slug=slug).first()
        u = p.user
        sent_friend_requests = FriendRequest.objects.filter(from_user=p.user)
        rec_friend_requests = FriendRequest.objects.filter(to_user=p.user)
        user_posts = Post.objects.filter(user_name=u)

        friends = p.friends.all()

        # is this user our friend
        button_status = "none"
        if p not in self.request.user.profile.friends.all():
            button_status = "not_friend"

            # if we have sent him a friend request
            if (
                len(
                    FriendRequest.objects.filter(from_user=request.user).filter(
                        to_user=p.user
                    )
                )
                == 1
            ):
                button_status = "friend_request_sent"

            # if we have recieved a friend request
            if (
                len(
                    FriendRequest.objects.filter(from_user=p.user).filter(
                        to_user=self.request.user
                    )
                )
                == 1
            ):
                button_status = "friend_request_received"

        context = {
            "u": u,
            "button_status": button_status,
            "friends_list": friends,
            "sent_friend_requests": sent_friend_requests,
            "rec_friend_requests": rec_friend_requests,
            "post_count": user_posts.count,
        }

        return render(request, "registration/profile1.html", context)


class My_Profille(View):
    def get(self, request, slug):
        p = self.request.user.profile
        you = p.user
        sent_friend_requests = FriendRequest.objects.filter(from_user=you)
        rec_friend_requests = FriendRequest.objects.filter(to_user=you)
        user_posts = Post.objects.filter(user_name=you)
        friends = p.friends.all()
        button_status = "none"
        if p not in self.request.user.profile.friends.all():
            button_status = "not_friend"
            if (
                len(
                    FriendRequest.objects.filter(from_user=self.request.user).filter(
                        to_user=you
                    )
                )
                == 1
            ):
                button_status = "friend_request_sent"
            if (
                len(
                    FriendRequest.objects.filter(from_user=p.user).filter(
                        to_user=self.request.user
                    )
                )
                == 1
            ):
                button_status = "friend_request_received"

            def get_context_data(self, **kwargs):
                context = super(My_Profille, self).get_context_data(**kwargs)
                context = self.get_context_data(object=self.object)

        context = {
            "u": you,
            "button_status": button_status,
            "friends_list": friends,
            "sent_friend_requests": sent_friend_requests,
            "rec_friend_requests": rec_friend_requests,
            "post_count": user_posts.count,
        }
        return render(request, "registration/profile1.html", context)


class SearchView(ListView):
    model = User
    context_object_name = "users"
    template_name = "registration/search_users.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            object_list = User.objects.filter(username__icontains=query)
            return object_list

