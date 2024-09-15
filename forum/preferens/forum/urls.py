from django.urls import path
from . import views

urlpatterns = [
    path('',  views.home, name="home"),
    path('TopPublished/',  views.top_pub, name="top"),
    path('TimePublished/',  views.time_pub, name="time"),
    path('search/',  views.search_pub, name="search"),
    path('<int:post_id>/', views.post_inp, name="post"),
]