from django.shortcuts import render

from .models import Post


def home(request):
    # o [:5] serve para limitar a 5 consultas
    posts = Post.objects.order_by('-data_publicacao')[:5]
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'post' : post,
    }
    return render(request, 'blog/post_detail.html', context)

def blog(request):
    return render(request, 'blog/blog.html')
