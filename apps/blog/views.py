from django.shortcuts import render, get_object_or_404
from apps.blog.models import Post
from apps.blog.filters import PostSearchFilter
from django.utils import timezone
from datetime import timedelta


def home(request):
    search = request.GET.get('qidirish')
    if search:
        posts = Post.objects.filter(title__icontains=search)
        return render(request, 'home.html', {'posts': posts})
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


def posts_by_category(request, category):
    filter = request.GET.get('filter_by')
    if filter:
        if filter == 'featured':
            posts = Post.objects.filter(category__slug=category, featured=True)
        elif filter == 'popular':
            posts = Post.objects.filter(category__slug=category).order_by('-views')
        elif filter == 'popular7days':
            try:
                posts = Post.objects.filter(category__slug=category, created_at__gte=timezone.now() - timedelta(days=7)).order_by('-views')
            except:
                posts = Post.objects.filter(category__slug=category)
        elif filter == 'random_posts':
            posts = Post.objects.filter(category__slug=category).order_by('?')
        return render(request, 'posts_by_category.html', {'posts': posts})
    posts = Post.objects.filter(category__slug=category)
    return render(request, 'posts_by_category.html', {'posts': posts})