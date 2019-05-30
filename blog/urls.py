from django.urls import path,re_path
from django.views.generic import ListView,DetailView
from blog.models import Post
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

