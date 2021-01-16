from django.shortcuts import render, get_object_or_404
from .models import Post, Tag

# Create your views here.

def index(request):
    posts   = Post.objects.order_by('-title')[:3]
    # tags    = Tag.objects.filter(posts = posts)
    context = {'posts' : posts}
    return render(request, 'blog/index.html', context)

def blog_posts(request):
    blog_posts = Post.objects.order_by('-title')[:4]
    context = {'blog_posts' : blog_posts}
    return render(request, 'blog/blog.html', context)

def single_posts(request):
    return render(request, 'blog/post.html')