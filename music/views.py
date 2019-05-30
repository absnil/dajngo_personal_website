from django.shortcuts import render
from .models import Song
from django.views.generic import ListView
# Create your views here.

class HomePageView(ListView):
	model=Song
	template_name='music.html'