from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from .forms import NewCommentForm, NewPostForm
from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comments
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import json
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views import generic

from braces.views import SelectRelatedMixin


class PostListView(ListView):
	model = Post
	template_name = 'feed/home.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 10
	def get_context_data(self, **kwargs):
		context = super(PostListView, self).get_context_data(**kwargs)
		return context

class UserPostListView(LoginRequiredMixin, ListView):
	model = Post
	template_name = 'feed/user_posts.html'
	context_object_name = 'posts'
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super(UserPostListView, self).get_context_data(**kwargs)
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return context

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(user_name=user).order_by('-date_posted')


@login_required
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	user = request.user
	if request.method == 'POST':
		form = NewCommentForm(request.POST)
		if form.is_valid():
			data = form.save(commit=False)
			data.post = post
			data.username = user
			data.save()
			return redirect('post-detail', pk=pk)
	else:
		form = NewCommentForm()
	return render(request, 'feed/post_detail.html', {'post':post,'form':form})



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['description', 'pic' ]
	template_name = 'feed/create_post.html'

	def form_valid(self, form):
		form.instance.user_name = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.user_name:
			return True
		return False

	

 


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy("home")

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Post Deleted")
        return super().delete(*args, **kwargs)



def like(request):
	post= get_object_or_404(Post, id= request.GET.get('post_id'))
	
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		is_liked=False
	else:
		post.likes.add(request.user)
		is_liked=True
	data = {
		'is_liked': is_liked,
		'total_likes': post.total_likes()
	}
	return JsonResponse(data)


class CreatePost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
   models = Post
   form_class = NewPostForm
   template_name='feed/create_post.html'
   success_url=reverse_lazy('home')
   def form_valid(self, form):
	   self.object = form.save(commit=False)
	   form.instance.user_name = self.request.user
	   self.object.user = self.request.user
	   self.object.save()
	   return super().form_valid(form)



	

