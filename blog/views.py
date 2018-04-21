from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, DetailView
from .models import Post, Comment
from .forms import NewPostForm, NewCommentForm
from accounts.models import User
from .decorators import blogger_required
from django.contrib.auth.decorators import login_required
# from django.contrib.auth import get_user_model
# User = get_user_model()


class HomeView(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'blog/posts.html'
	paginate_by = 10

class PostView(DetailView):
	model = Post
	context_object_name = 'post'
	template_name = 'blog/post.html'
	

class UserView(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'blog/blogger.html'
	paginate_by = 10

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['username'] = User.objects.get(username=self.kwargs['username'])
		return context

	def get_queryset(self):
		self.user = get_object_or_404(User, username=self.kwargs['username'])
		return Post.objects.filter(created_by=self.user).order_by('-created_at')

class UserListView(ListView):
	model = User
	context_object_name = 'users'
	template_name = 'blog/bloggers.html'
	paginate_by = 10


@blogger_required
def NewPostView(request):
	if request.method == 'POST':
		form = NewPostForm(request.POST)
		if form.is_valid():
			blog = form.save(commit=False)
			blog.created_by = request.user
			blog.save()
			return redirect('blog:blog', pk=blog.pk)
	else:
		form = NewPostForm()
	return render(request, 'blog/new.html', {'form': form})



def NewCommentView(request, pk):
	if request.user.is_authenticated :
		post = Post.objects.get(pk=pk)
		if request.method == 'POST':
			form = NewCommentForm(request.POST)
			if form.is_valid():
				comment = form.save(commit=False)
				comment.created_by = request.user
				comment.post = post
				comment.save()
				return redirect('blog:blog', pk=pk)
		else:
			form = NewCommentForm()
		return render(request, 'blog/comment.html', {'form': form, 'post': post})
	else:
		return redirect('accounts:login')

