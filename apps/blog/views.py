from django.shortcuts import render, get_object_or_404
from apps.blog.models import Category, Post


def home(request):
    return render(request, 'home.html')

def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, created_at__year=year, created_at__month=month, created_at__day=day)
    next_post = Post.objects.filter(created_at__gt=post.created_at).order_by('created_at').first()
    previous_post = Post.objects.filter(created_at__lt=post.created_at).order_by('-created_at').first()
    same_posts = Post.objects.filter(category=post.category).exclude(id=post.id).order_by('-created_at')
    same_owner_posts = Post.objects.filter(author=post.author).exclude(id=post.id).order_by('-created_at')
    context = {
        'post': post,
        'next_post': next_post,
        'previous_post': previous_post,
        'same_posts': same_posts,
        'same_owner_posts': same_owner_posts,
    }
    return render(request, 'post_detail.html', context)