from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import LoginForm, RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile

def uniqueEmail(username, email):
    users = User.objects.filter(email=email)
    if len(users) < 1 or users[0].username == username:
        return True
    return False

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome Back {user.first_name}")
                return redirect("main:home")

            else:
                messages.error(request, "Invalid Credentials.")
                return render(request, "users/login.html", {
            'form': form,
        })

        else:
            messages.error(request, "Invalid Credentials.")
            return render(request, "users/login.html", {
            'form': form,
        })

    return render(request, "users/login.html", {
            'form': LoginForm,
        })

def register_view(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            first_name = form.cleaned_data.get("first_name")
            if uniqueEmail(username, email):
                if len(first_name) > 2:
                    user = form.save()
                    login(request, user)
                    messages.success(request, f"You are Most Welcome {first_name}")
                    return redirect("main:home")
                else:
                    messages.error(request, "First Name is Required.")
                    return render(request, "users/register.html", {
                        'form': form,
                    })
            else:
                messages.error(request, "This Email is already taken.")
                return render(request, "users/register.html", {
                    'form': form,
                })

        else:
            return render(request, "users/register.html", {
            'form': form,
        })

    return render(request, "users/register.html", {
            'form': RegisterForm,
        })

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have Logged Out Securely.')
    return redirect("main:home")

@login_required
def profile(request):
    return render(request, "users/profile.html")

@login_required
def profile_update(request):
    if request.method == 'POST':
        previous_username = request.user.username
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid() and p_form.is_valid():
            if uniqueEmail(request.user.username, u_form.cleaned_data.get('email')) == True:
                u_form.save()
                p_form.save()
                messages.success(request, 'Your profile has been updated.')
                return redirect('users:profile')
            else:
                messages.error(request, 'This Email is already taken.')
                return redirect('users:profile_update')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'p_form':p_form,
        'u_form':u_form,
    }
    return render(request, 'users/profile_update.html', context)
