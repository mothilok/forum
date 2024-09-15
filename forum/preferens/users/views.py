from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from forum.models import Posts


def registration(request):
    post_request = request.POST
    if post_request:
        create_us = User.objects.create_user(username=post_request['user_name'], email=post_request['email'], password=post_request['password'])
        auth = authenticate(username=post_request['user_name'], password=post_request['password'])
        if auth is not None:
            login(request, auth)
    us_name = request.user
    if post_request:
        return redirect(reverse('home'))
    context = {
        "user_name":us_name
    }
    return render(request, 'users/registretion.html', context)

def login_user (request):
    post_request = request.POST
    if post_request:
        auth = authenticate(username=post_request['user_name'], password=post_request['password'])
        if auth is not None:
            login(request, auth)
    return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    return render(request, 'users/logout.html')

def create_post(request):
    post_request = request.POST
    if not request.user.is_authenticated:
        return redirect(reverse('login'), permanent=True)
    if post_request:
        if post_request['title']:
            create_published = Posts(title=post_request['title'], text_post=post_request['text_post'], author=request.user).save()
    return render(request, 'users/create_post.html')
