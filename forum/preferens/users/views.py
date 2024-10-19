from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from forum.models import Posts


def registration(request):
    if request.POST:
        User.objects.create_user(username=request.POST['user_name'], email=request.POST['email'], password=request.POST['password'])
        auth = authenticate(username=request.POST['user_name'], password=request.POST['password'])
        if auth is not None:
            login(request, auth)
    us_name = request.user
    if request.POST:
        return redirect(reverse('home'))
    context = {
        "user_name":us_name
    }
    return render(request, 'users/registretion.html', context)

def login_user (request):
    if request.POST:
        auth = authenticate(username=request.POST['user_name'], password=request.POST['password'])
        if auth is not None:
            login(request, auth)
    return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    return render(request, 'users/logout.html')

def create_post(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'), permanent=True)
    if request.method == "POST":
        Posts(title=request.POST['title'], text_post=request.POST['text_post'], author=request.user, image=request.FILES['image']).save()
    return render(request, 'users/create_post.html')

