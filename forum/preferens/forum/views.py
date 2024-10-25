from django.shortcuts import render, redirect
from .models import Posts, Array_Like, Whitelist, Pars_files
from django.db.models import F
from django.urls import reverse
from django.http import HttpResponse
import re
import hashlib


def home(request):
    us_name = request.user
    context = {
        'user_name':us_name
    }
    return render(request, "forum/home.html", context)

def post_inp(request, post_id):
    like(request, post_id)
    request_db = Pars_files.objects.filter(key_posts_id=post_id)[0]
    file = request_db.file
    print(file.name)


    data = Posts.objects.get(id=post_id)
    context = {
        "data":data,
        'file':file
    }
    return render(request, "forum/post.html", context)

def top_pub (request):
    top_post = Posts.objects.order_by("-votes")[:5]
    context = {
        "top_post":top_post
    }
    return render(request, "forum/top_pub_t.html", context)

def time_pub (request):
    time_post = Posts.objects.order_by("-data_published")[:5]
    context = {
        "time_post":time_post
    }
    return render(request, "forum/time_pub_t.html", context)

def search_pub (request):
    if request.POST:
        search_resalt = Posts.objects.filter(title=request.POST['request_from_template'])
        response_length = len(search_resalt)
    else:
        search_resalt = None
        response_length = None
    context = {
        "search_resalt":search_resalt,
        "response_length":response_length
    }
    return render(request, "forum/search_t.html", context)

def create_post(request):# TO DO сделать прием post запр файла на pars_files
    if not request.user.is_authenticated:
        return redirect(reverse('login'), permanent=True)
    if request.method == "POST":
        Posts(title=request.POST['title'], text_post=request.POST['text_post'], author=request.user,).save()
        id_post = Posts.objects.order_by('-id')[0].id # мне это не нравится
        print(id_post)
        if request.FILES['image']:
            name = str(re.findall('.{1,100}[.]', request.FILES['image'].name)[0][:-1])
            format_files = str(re.findall('[.]\w{3,5}\\b', str(request.FILES["image"]))[-1]).upper()
            file = request.FILES['image']
            file.name = name
            print(file)
            print(type(file.name))
            hash_name = hashlib.md5(name.encode()).hexdigest()
            print(type(name))
            print(hash_name)
            print(Whitelist.objects.get(files_format=format_files))
            if Whitelist.objects.get(files_format=format_files):
                Pars_files(file=file, format=format_files, hash_name=hash_name, key_posts_id=id_post).save()
            else:
                return HttpResponse('<h3>Недопустимый формат файла</h3>')


    return render(request, 'forum/create_post.html')

#сделать парс формата с пом вайт листа и вайт лист распределить по файлам наприм изобр

def like(request, id_objetct):
    if request.user.is_authenticated:
        if request.POST:
            id_user = request.user.id
            try:
                check_like = Array_Like.objects.get(id_post=id_objetct, id_user=id_user)
            except:
                check_like = False
            if check_like:
                Posts.objects.filter(id=id_objetct).update(votes= F("votes") - 1)
                Array_Like.objects.filter(id_post=id_objetct, id_user=id_user).delete()
            else:
                Posts.objects.filter(id=id_objetct).update(votes=F("votes") + 1)
                Array_Like(id_post=id_objetct, id_user=id_user).save()
