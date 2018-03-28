from django.test import TestCase
from .models import Post
from accounts.models import User
from .views import HomeView
from django.urls import reverse, resolve
class HomeTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='john', email='john@doe.com', password='123')
        self.blog = Post.objects.create(
            title='Blog Title', content='Blog Description.', created_by=self.user)
        url = reverse('blog:home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, HomeView)

    def test_home_view_contains_link_to_blog_page(self):
        blog_url = reverse('blog:blog', kwargs={
                              'pk': self.blog.id})
        self.assertContains(self.response, 'href="{0}"'.format(blog_url))


class BloggerAuthorizedHomeTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='john', email='john@doe.com', password='123')
        self.blog = Post.objects.create(
            title='Blog Title', content='Blog Description.', created_by=self.user)
        self.response = self.client.get(reverse('blog:home'))

    def test_home_view_contains_new_blog_link(self):
        new_blog_url = reverse('blog:new')
        self.assertContains(self.response, 'href="{0}"'.format(new_blog_url))
