
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('accounts/signup/', views.SignUp, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
]
