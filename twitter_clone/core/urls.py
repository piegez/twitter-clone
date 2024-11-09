from django.urls import path
from .views import RegisterView, feed, LoginView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('feed/', feed, name='feed'),
    path('login/', LoginView.as_view(), name='login'),
]
