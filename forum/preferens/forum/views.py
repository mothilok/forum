from django.shortcuts import render
from .models import Posts, Array_Like
from django.db.models import F


def home(request):
    us_name = request.user
    context = {
        'user_name':us_name
    }
    return render(request, "forum/home.html", context)

def post_inp(request, post_id):
    like(request, post_id)
    post_out = Posts.objects.get(id=post_id)
    context = {
        "post_out":post_out
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
    post_requtst = request.POST
    print(post_requtst)
    if post_requtst:
        search_resalt = Posts.objects.filter(title=post_requtst['request_from_template'])
        response_length = len(search_resalt)
    else:
        search_resalt = None
        response_length = None
    context = {
        "search_resalt":search_resalt,
        "response_length":response_length
    }
    return render(request, "forum/search_t.html", context)

def like(request, id_objetct):
    post_request = request.POST
    print(post_request)
    if request.user.is_authenticated:
        if post_request:
            id_user = request.user.id
            try:
                check_like = Array_Like.objects.get(id_post=id_objetct, id_user=id_user)
            except:
                check_like = False
            if check_like:
                lower_like = Posts.objects.filter(id=id_objetct).update(votes= F("votes") - 1)
                delete_to_Arr = Array_Like.objects.filter(id_post=id_objetct, id_user=id_user).delete()
            else:
                raise_like = Posts.objects.filter(id=id_objetct).update(votes=F("votes") + 1)
                write_to_Arr = Array_Like(id_post=id_objetct, id_user=id_user).save()
