from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('blog/<int:pk>/', views.PostView.as_view(), name='post'),
    path('blogger/<username>/', views.UserView.as_view(), name='blogger'),
    path('bloggers/', views.UserListView.as_view(), name='bloggers')
]
