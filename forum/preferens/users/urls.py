from django.urls import path
from . import views


urlpatterns = [
    path('registration/', views.registration, name='registr'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('create_publused/', views.create_post, name='create_post')
]

