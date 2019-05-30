from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.order_by('date')
    return render(request, 'blog/blog.html', {'posts': posts})