from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('search-results/', views.SearchResults.as_view(), name='search-results'),
    path('search/', views.SearchView, name='search'),
    path('blog/<int:pk>/', views.PostView.as_view(), name='blog'),
    path('blog/new/', views.NewPostView, name='new'),
    path('blog/<int:pk>/comment/', views.NewCommentView, name='comment'),
    path('blogger/<username>/', views.UserView.as_view(), name='blogger'),
    path('bloggers/', views.UserListView.as_view(), name='bloggers')
]
