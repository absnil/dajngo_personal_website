from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

# Create your views here.
from .models import Post


class HomePageView(ListView):
	model=Post
	template_name='comics.html'