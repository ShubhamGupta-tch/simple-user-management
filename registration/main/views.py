from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):
    return render(request, "main/index.html", {
            'users': User.objects.all()
        })

def profile(request, username):
    user = User.objects.get(username=username)
    if user == request.user:
        return redirect('users:profile')
    return render(request, 'users/user_profile.html', {'u':user})
