# core/urls.py
from django.urls import path
from .views import RegisterView, feed, LoginView  # Não se esqueça de importar LoginView aqui

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('feed/', feed, name='feed'),
    path('login/', LoginView.as_view(), name='login'),  # URL do Login
]
