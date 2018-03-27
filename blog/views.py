from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from .models import Post, Comment
from accounts.models import User

class HomeView(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'blog/posts.html'
	paginate = 10


class PostView(TemplateView):
	template_name = 'blog/post.html'
	
	def get_context_data(self, **kwargs) :
		context = super().get_context_data(**kwargs)
		context['post'] = Post.objects.get(pk = self.kwargs['pk'])	 
		context['comments'] = Comment.objects.filter(post = self.kwargs['pk'])
		return context


class UserView(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'blog/blogger.html'
	paginate = 10

	def get_context_data(self, **kwargs):
		return super().get_context_data(**kwargs)

	def get_queryset(self):
		self.user = get_object_or_404(User, username=self.kwargs['username'])
		return Post.objects.filter(created_by=self.user).order_by('-created_at')

class UserListView(ListView):
	model = User
	context_object_name = 'users'
	template_name = 'blog/bloggers.html'
	paginate = 10

