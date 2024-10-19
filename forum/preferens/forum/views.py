from django.shortcuts import render, redirect
from .models import Posts, Array_Like
from django.db.models import F
from django.urls import reverse


def home(request):
    us_name = request.user
    context = {
        'user_name':us_name
    }
    return render(request, "forum/home.html", context)

def post_inp(request, post_id):
    like(request, post_id)
    data = Posts.objects.get(id=post_id)
    context = {
        "data":data
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

    print(request.POST)
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

def create_post(request):
    if not request.user.is_authenticated:
        return redirect(reverse('login'), permanent=True)
    if request.method == "POST":
        Posts(title=request.POST['title'], text_post=request.POST['text_post'], author=request.user,
              image=request.FILES['image']).save()
    return render(request, 'forum/create_post.html')

def like(request, id_objetct):
    print(request.POST)
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
