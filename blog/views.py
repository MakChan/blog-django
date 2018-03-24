from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Post, Comment

class HomeView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/posts.html'


class PostView(TemplateView):
    template_name = 'blog/post.html'
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['post'] = Post.objects.get(pk = self.kwargs['pk'])	 
        context['comments'] = Comment.objects.filter(post = self.kwargs['pk'])
        return context
