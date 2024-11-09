# core/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Tweet
from .serializers import UserSerializer


class RegisterView(APIView):
    def get(self, request):
        return render(request, 'core/signup.html')

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('login')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def get(self, request):
        return render(request, 'core/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        return render(request, 'core/login.html', {'error': 'Credenciais inválidas'})


@login_required
def feed(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        Tweet.objects.create(user=request.user, content=content)
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'core/feed.html', {'tweets': tweets})
