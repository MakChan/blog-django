from django.db import models
from django.contrib.auth.models import User
from project_blog import settings

from django.utils.html import mark_safe
from markdown import markdown

class Post(models.Model) :
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='posts', on_delete=models.CASCADE)

    def get_post_as_markdown(self):
        return mark_safe(markdown(self.content, safe_mode='escape'))
    class Meta:
        ordering = ['-created_at']


class Comment(models.Model) :
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post, related_name='comments', on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name='comments', on_delete=models.CASCADE)
