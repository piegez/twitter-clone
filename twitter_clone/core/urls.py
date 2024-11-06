# core/urls.py
from django.urls import path
from .views import RegisterView, LoginView, feed

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('feed/', feed, name='feed'),
]
